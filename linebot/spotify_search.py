import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentialselse

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
            return artist['images'][0]['url']


    def spotify_sample_audio(slef, name):

        spotify = self.spotify_security()
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
