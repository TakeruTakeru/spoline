from django.shortcuts import render
from django.http import HttpResponse
import json
import random
import requests
from .spotify_search import taketify
import re

REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'
ACCESS_TOKEN = 'bdtGx1Xb7CIqX3mFQCDgzjuVPt8kMbs+ZinutU4QsCiXiJfrO7EzXv7N8eF1vilzCWN6HVEAh2ldyZCokoGki0GVVpnrmQcVv1NxuWN9xKP+93xU5+ZtH01BT0R3BXjkFUmpmZ3d/YSSJSU0qgdFRgdB04t89/1O/w1cDnyilFU='
HEADER = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + ACCESS_TOKEN
}

def index(request):
    return HttpResponse("This is bot api.")

def reply_image(reply_token, text, name):
    artist = name
    reply = taketify.spotify_image(artist)
    payload = {
          "replyToken":reply_token,
          "messages":[
                {
                    "type":"image",
                    "originalContentUrl": reply,
                    "previewImageUrl": reply,
                }
            ]
    }

    requests.post(REPLY_ENDPOINT, headers=HEADER, data=json.dumps(payload)) # LINEにデータを送信
    return reply

def reply_sample(reply_token, text, name):
    artist = name
    url_before = taketify.spotify_sample_audio(artist)
    reply = url_before.replace("?cid=e6447eec6f8448d7a80b1c45a8237034", "")
    payload = {
          "replyToken":reply_token,
          "messages":[
                {
                    "type":"text",
                    "text":reply
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
        message_type = e['message']['type']   # typeの取

        if message_type == 'text':
            text = e['message']['text']
            text_check = re.match(r"^画像", text)
            if text_check:
                image = text.replace("画像", "")
                reply += reply_image(reply_token, image, image)  # LINEにセリフを送信する関数
            else:
                reply += reply_sample(reply_token, text, text)
    return HttpResponse(reply)

# 先ほどのおそ松のセリフ一覧をimport
