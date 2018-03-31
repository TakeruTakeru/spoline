from django.http import HttpResponse
import json
import requests
from .spotify_search import taketify, Goodbye, LineBotApi
import re
import os
from pykakasi import kakasi

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

    if reply == False:
        reply = "ごめんなさい、その人は知らないなぁ。。"
        payload = {
              "replyToken":reply_token,
              "messages":[
                    {
                        "type":"text",
                        "text":reply
                    }
                ]
        }
    else:
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

    requests.post(REPLY_ENDPOINT, headers=HEADER, data=json.dumps(payload))
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

    requests.post(REPLY_ENDPOINT, headers=HEADER, data=json.dumps(payload))
    return reply


def callback(request):
    '''
    '''
    reply = ""
    request_json = json.loads(request.body.decode('utf-8'))
    for e in request_json['events']:
        reply_token = e['replyToken']
        message_type = e['message']['type']
        if e["source"]["type"] != "user" and message_type == "text":
            print("check")
            check = Goodbye()
            text = e["message"]["text"]
            judge = check.check(text)

            if judge == True and e["source"]["type"] == "group":
                group_id = e["source"]["groupId"]
                check_out = LineBotApi()
                check_out.leave_group(group_id)

            if judge == True and e["source"]["type"] == "room":
                room_id = e["source"]["roomId"]
                check_out = LineBotApi()
                check_out.leave_room(room_id)


        if message_type == 'text':
            text = e['message']['text']
            text_check = re.match(r"^画像", text)
            if text_check:
                image = text.replace("画像", "")
                reply += reply_image(reply_token, image, image)
            else:
                reply += reply_sample(reply_token, text, text)

    return HttpResponse(reply)
