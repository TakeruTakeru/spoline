
class taketify():

    import spotipy
    from spotipy.oauth2 import SpotifyClientCredentials


    client_id = 'e6447eec6f8448d7a80b1c45a8237034'
    client_secret = '98e4103299954b18a51fa991db7d6741'
    client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


    def spotify_image(name):

        search_str = name
        result = spotify.search(q="artist:" + search_str, limit=1, type="artist")
        item = result["artists"]["items"]
        image_url = item["images"]["url"]
        return image_url

    def spotify_name(name):

        search_str = name
        result = spotify.search(q="artist:" + search_str, limit = 1, type="artist")
        item = result["artists"]["items"]
        name = item["name"]
        return name
