import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials



class taketify(spotipy.Spotify):


    def spotify_image(name):

        client_id = os.environ["SPOTIFY_CLIENT_ID"]
        client_secret = os.environ["SPOTIFY_CLIENT_SECRET"]
        client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
        spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        search_str = name
        result = spotify.search(q="artist:" + search_str, limit=1, type="artist")
        item = result["artists"]["items"]
        if len(item) > 0:
            artist = item[0]
            return artist['images'][0]['url']

    def spotify_name(name):

        search_str = name
        result = spotify.search(q="artist:" + search_str, limit = 1, type="artist")
        item = result["artists"]["items"]
        if len(item) > 0:
            artist = item[0]
            return artist["name"]

    def spotify_sample_audio(name):

        client_id = os.environ["SPOTIFY_CLIENT_ID"]
        client_secret = os.environ["SPOTIFY_CLIENT_SECRET"]
        client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
        spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        search_str = name
        result = spotify.search(q="artist:" + search_str, limit=1, type="artist")
        item = result["artists"]["items"]
        if len(item) > 0:
            af = item[0]
            theid = af["id"]
            results = spotify.artist_top_tracks(theid)
            items = results["tracks"][:3]
            a = ""
            for i in reversed(items):
                if i["preview_url"]:
                    a = i["preview_url"]
            if a == "":
                a = "Sorry, no contents has been detected.."
        return a


    def spotify_sample_image(name):

        search_str = name
        results = spotify.artist_top_tracks(search_str)
        items = results["tracks"][:1]
        return items["album"]["images"][0]["url"]
