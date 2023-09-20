import requests
import spotipy
import applemusicpy
from spotipy.oauth2 import SpotifyOAuth
from tqdm import tqdm


# Client ID info for Apple
apple_private_key = """-----BEGIN PRIVATE KEY-----
MIGTAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBHkwdwIBAQQgdJWWRce9ukBKyeGs
du4RebPYowNKbe6yFolj0QSURs6gCgYIKoZIzj0DAQehRANCAAQhl/lV5IXgaWmp
t7ib3taG3jyte1J2vsgS6pkX0l74tpvJ/Lx5goOz57S8jZ0/scfhmZc8n85kHafi
6F3VH3QB
-----END PRIVATE KEY-----"""
apple_key_id = input("Apple Key ID: ")
apple_team_id = input("Apple Team ID: ")

am = applemusicpy.AppleMusic(secret_key=apple_private_key, key_id=apple_key_id, team_id=apple_team_id)


# Client ID info for Spotify
client_id = input("Spotify Client ID: ")
client_secret = input("Spotify Secret Client ID: ")
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

# For Account Modifications:
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope='playlist-modify-private'))

user_id = 'yd1000'

playlist_name = 'ConvertTest'

new_playlist = sp.user_playlist_create(user_id, playlist_name, public=False)

print(f'Created playlist: {new_playlist["name"]} (ID: {new_playlist["id"]})')

playlist_id = new_playlist["id"]

# For Playlist access via URI
sp2 = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope='playlist-read-private'))
playlist_uri = 'spotify:playlist:61yNGARBrHdNE2GFFT1Mr5'
playlist = sp2.playlist_tracks(playlist_uri)

#Create Track Array for Spotify
spotify_tracks = []
offset = 0
limit = 100

playlist_info = sp.playlist(playlist_uri)
total_tracks = playlist_info['tracks']['total']

# Create a tqdm progress bar
while True:
    playlist_tracks = sp.playlist_tracks(playlist_uri, offset=offset, limit=limit)
    spotify_tracks += playlist_tracks['items']
    if not playlist_tracks['next']:
        break
    offset += limit

# Reset the offset for adding tracks to the playlist
offset = 0

# Use a second tqdm progress bar while adding tracks to the playlist
with tqdm(total=len(spotify_tracks), unit='track') as pbar:
    for track in spotify_tracks:
        track_uri = track['track']['uri']
        sp.playlist_add_items(playlist_id, [track_uri])
        offset += 1
        pbar.update(1)

print(f'Added {offset} tracks to the playlist.')





# Apple Music Creation
