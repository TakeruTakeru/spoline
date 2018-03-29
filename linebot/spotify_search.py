import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pykakasi import kakasi
import re

class taketify(spotipy.Spotify):

    def spotify_security(self):

        client_id = os.environ["SPOTIFY_CLIENT_ID"]
        client_secret = os.environ["SPOTIFY_CLIENT_SECRET"]
        client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
        spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        return spotify


    def spotify_image(self, name):

        spotify = self.spotify_security()
        search_str = name
        result = spotify.search(q="artist:" + search_str, limit=1, type="artist")
        item = result["artists"]["items"]
        if len(item) > 0:
            artist = item[0]
            image_url = artist['images'][0]['url']
        else:
            image_url = False

        return image_url

    def spotify_sample_audio(self, name):

        spotify = self.spotify_security()
        search_str = name
        result = spotify.search(q="artist:" + search_str, limit=1, type="artist")
        item = result["artists"]["items"]
        if len(item) > 0:
            af = item[0]
            theid = af["id"]
            results = spotify.artist_top_tracks(theid)
            items = results["tracks"][:5]
            a = ""
            for i in reversed(items):
                if i["preview_url"]:
                    a = i["preview_url"]
            if a == "":
                a = "そのアーティストの曲はないみたいだなぁ。。。"
        else:
            a = "呼んだ？！\n あ、呼んでない？ごめんごめん。"
        return a


class Goodbye(pykakasi.kakasi):

    def kakasi_set(self, target):
        target = str(target)
        kaka = kakasi()
        kaka.setMode('H', 'a')
        kaka.setMode('K', 'a')
        kaka.setMode('J', 'a')
        conv = kaka.getConverter()
        text = conv.do(target)
        return text

    def check(self, chat):
        waruguchi = [
        'gm', 'bai', 'bye', 'www', 'sine', 'gomi',
         'kunna', 'deteke', 'kikasaru', 'sayonara',
         'sarusine', 'tukaenai'
         ]
         text_sent = self.kakasi_set(chat)
         flag = False
         for i in waruguchi:
             if re.search(i, text_sent):
                 flag = True
