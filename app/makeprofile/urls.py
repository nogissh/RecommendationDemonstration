from django.urls import path

from . import views


app_name = 'makeprofile'
urlpatterns = [
  path('', views.index, name="index"),
  path('form/', views.form, name="form"),
  path('regist/', views.regist, name="regist"),
]
