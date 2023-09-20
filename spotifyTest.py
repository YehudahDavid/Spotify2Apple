import requests
import spotipy
import applemusicpy
from spotipy.oauth2 import SpotifyOAuth
from tqdm import tqdm

# Client ID info for Spotify
client_id = "0224ab959e5c4e2696331ef1499cd03c"
client_secret = "236c368e6ecb4a9b9d7d12beb5836db3"
redirect_uri = 'http://localhost:8080'

auth_url = 'https://accounts.spotify.com/api/token'

data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
}

auth_response = requests.post(auth_url, data=data)
# Get Access Token
access_token = auth_response.json().get('access_token')

sp2 = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope='playlist-read-private'))
playlist_uri = 'spotify:playlist:7us4ie2YBpppkzq4JFMRAW'
playlist = sp2.playlist_tracks(playlist_uri)

for song in playlist['items']:
    print(song['track']['external_ids']['isrc'])