import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
from time import time
import os
import json
import time
import spotipy

os.environ['SPOTIPY_CLIENT_ID']='80d546f8fec24b6c9d5f957f194dd8fd'
os.environ['SPOTIPY_CLIENT_SECRET']='260b1cf5f4ca41eb9ebe0db298f9bf0e'
os.environ['SPOTIPY_REDIRECT_URI']='http://google.com/'



spotify_client_id = os.environ['SPOTIPY_CLIENT_ID']
spotify_secret = os.environ['SPOTIPY_CLIENT_SECRET']
spotify_redirect_uri = os.environ['SPOTIPY_REDIRECT_URI']

scope = 'user-read-currently-playing'

oauth_object = spotipy.SpotifyOAuth(client_id=spotify_client_id,
                                    client_secret=spotify_secret,
                                    redirect_uri=spotify_redirect_uri,
                                    scope=scope)

token_dict=oauth_object.get_access_token()
token = token_dict['access_token']
print(token)



# spotify object
sp = spotipy.Spotify(auth=token)

playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF?si=1333723a6eff4b7f"
playlist_URI = playlist_link.split("/")[-1].split("?")[0]
track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]

