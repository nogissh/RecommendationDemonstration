import datetime, json


def make_message(state   : bool,
                  message : str,
                  content=None) -> dict:
  """
  返答メッセージを生成
  """
  message = {
    "state": state,
    "message": message,
    "content": content,
  }

  return message


def json_serial(obj: dict) -> dict:
  """
  date, datetimeの変換関数
  """

  # 日付型の場合には、文字列に変換します
  if isinstance(obj, (datetime.datetime, datetime.date, datetime.time)):
    return obj.isoformat()
  raise TypeError ("Type %s not serializable" % type(obj)) #上記以外はサポート対象外.
