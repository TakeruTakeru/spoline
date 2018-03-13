from django.shortcuts import render
from django.http import HttpResponse
import json
import random
import requests
from .spotify_search import taketify
import re
import os

REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'
ACCESS_TOKEN = os.environ["LINE_TOKEN"]

HEADER = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + ACCESS_TOKEN
}

def index(request):
    return HttpResponse("This is bot api.")

def reply_image(reply_token, text, name):
    artist = name
    rep = taketify()
    reply = rep.spotify_image(artist)
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
    url_before_before = taketify()
    url_before = url_before_before.spotify_sample_audio(artist)
    client_id = os.environ["SPOTIFY_CLIENT_ID"]
    del_str = "?cid=" + client_id
    reply = url_before.replace(del_str, "")
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
