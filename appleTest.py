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
apple_key_id = "2TQCT3A8G5"
apple_team_id = "27YLH627PZ"

am = applemusicpy.AppleMusic(secret_key=apple_private_key, key_id=apple_key_id, team_id=apple_team_id)
results = am.search('travis scott', types=['albums'], limit=5)
for item in results['results']['albums']['data']:
    print(item['attributes']['name'])