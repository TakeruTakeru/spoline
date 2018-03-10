from django.shortcuts import render
from django.http import HttpResponse
import json
import random
import requests
from .load_serif import osomatsu_serif

REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'
ACCESS_TOKEN = 'bdtGx1Xb7CIqX3mFQCDgzjuVPt8kMbs+ZinutU4QsCiXiJfrO7EzXv7N8eF1vilzCWN6HVEAh2ldyZCokoGki0GVVpnrmQcVv1NxuWN9xKP+93xU5+ZtH01BT0R3BXjkFUmpmZ3d/YSSJSU0qgdFRgdB04t89/1O/w1cDnyilFU='
HEADER = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + ACCESS_TOKEN
}

def index(request):
    return HttpResponse("This is bot api.")

def reply_text(reply_token, text):
    reply = "https://i.scdn.co/image/f3dd808a2eff56552da545beb5b0fc5d3892817a"
    payload = {
          "replyToken":reply_token,
          "messages":[
                {
                    "type":"text",
                    "text": reply
                }
            ]
    }

    requests.post(REPLY_ENDPOINT, headers=HEADER, data=json.dumps(payload)) # LINEにデータを送信
    return reply

def callback(request):
    reply = ""
    request_json = json.loads(request.body.decode('utf-8')) # requestの情報をdict形式で取得
    for e in request_json['events']:
        reply_token = e['replyToken']  # 返信先トークンの取得
        message_type = e['message']['type']   # typeの取得

        if message_type == 'text':
            text = e['message']['text']    # 受信メッセージの取得
            reply += reply_text(reply_token, text)   # LINEにセリフを送信する関数
    return HttpResponse(reply)

# 先ほどのおそ松のセリフ一覧をimport
