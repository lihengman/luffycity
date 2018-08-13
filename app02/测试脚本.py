import json
import requests

# 1.伪造浏览器https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential... 发送GET请求,并获取token
r1 = requests.get(
    url = "https://api.weixin.qq.com/cgi-bin/token",
    params={
        "grant_type": "client_credential",
        "appid": "wx13328dfbb0585940",
        "secret": "ddae71dfaa53e6546b20550b2e46c5dd"
    }
)

access_token = r1.json().get("access_token")

# 2.给指定用户发送普通消息: access_token/
"""
wx_id = "oaV3Z5jivfnvRHJrXKqhe3LaUTu4"

body = {
    "touser": wx_id,
    "msgtype": "text",
    "text": {
        "content": "欢迎 "
    }
}

r2 = requests.post(
    url="https://api.weixin.qq.com/cgi-bin/message/custom/send",
    params={
        'access_token': access_token
    },
    data=bytes(json.dumps(body, ensure_ascii=False), encoding='utf-8')
)

print(r2.text)
"""

# 3.给指定用户发送模板消息: access_token/

wx_id = "oaV3Z5jivfnvRHJrXKqhe3LaUTu4"

body = {
    "touser": wx_id,
    "template_id":	'L1ZoEifaOlhgudUPhw5LvQNdYKdqjz4-scEKR2Aakek',
    "data": {
        "user": {
            "value": "樱花雨",
            "color": "#173177"
        }
    }
}

r2 = requests.post(
    url="https://api.weixin.qq.com/cgi-bin/message/template/send",
    params={
        'access_token':access_token
    },
    data=json.dumps(body)
)

print(r2.text)

response = requests.post(
    url="https://api.weixin.qq.com/cgi-bin/message/custom/send",
    params={
        'access_token': access_token
    },
    data=bytes(json.dumps(body, ensure_ascii=False), encoding='utf-8')
)
# 这里可根据回执code进行判定是否发送成功(也可以根据code根据错误信息)
result = response.json()
print(result)