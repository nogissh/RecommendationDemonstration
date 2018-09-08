from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import UserProfile

import json
from generaltools.tools import (
  make_message,
)


def index(request):
  return render(request, 'makeprofile/index.html')


def form(request):

  # name
  content = {
    'code': request.POST.get('code', ''),
    'name': request.POST.get('name', ''),
  }

  # 未回答を拒否
  if '' == content['name']:
    message = make_message(False, "名前を入力してください。")
    return render(request, 'makeprofile/error.html', message)

  # メッセージを生成
  message = make_message(True, message='success!', content=content)

  return render(request, 'makeprofile/form.html', message)


def regist(request):

  # to dict
  content = {
    'code': request.POST.get('code', ''),
    'name': request.POST.get('name', None),
    'q1'  : request.POST.get('q1', None),
    'q2'  : request.POST.get('q2', None),
    'q3'  : request.POST.get('q3', None),
    'q4'  : request.POST.get('q4', None),
    'q5'  : 1,
  }

  # 未回答を拒否
  if None in content.values():
    message = make_message(False, 'すべての設問に回答してください。')
    return render(request, 'makeprofile/error.html', message)

  # regist new profile
  new_uProfile = UserProfile(
    code=content['code'],
    name=content['name'],
    q1=content['q1'],
    q2=content['q2'],
    q3=content['q3'],
    q4=content['q4'],
    q5=content['q5'],
  )
  new_uProfile.save()

  # オブジェクトを生成
  message = make_message(True, message='success!', content=content)

  return render(request, 'makeprofile/thanks.html', message)
