import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import re


CLIENT_ID = ''
CLIENT_SECRET = ''
REDIRECT_URI = 'http://localhost:8888/callback/'
USERNAME = ''
PLAYLIST_ID = ''

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=REDIRECT_URI,scope='playlist-modify-private playlist-modify-public',username=USERNAME))

def regexSongName(songName):
    cleanname=re.sub(r'^\d+\s*|\[.*?\]','',songName)
    return cleanname.strip()

def extractsongname(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
        songNames = [regexSongName(os.path.splitext(os.path.basename(line.strip()))[0]) for line in lines]
    return songNames





songstoadd=extractsongname('songs.txt')


for i,songname in enumerate(songstoadd):
    results = sp.search(q=songname,type='track',limit=1)
    if results['tracks']['items']:

        trackuri = results['tracks']['items'][0]['uri']
        sp.playlist_add_items(playlist_id=PLAYLIST_ID, items=[trackuri])
        print(f"[{i}] Added '{songname}' to the playlist.")

    else:print(f"Could not find '{songname}' on Spotify.")
print("Playlist update complete.")
