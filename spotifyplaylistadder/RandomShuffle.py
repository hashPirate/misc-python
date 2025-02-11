import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random

CLIENT_ID = ''
CLIENT_SECRET = ''
REDIRECT_URI = 'http://localhost:8888/callback/'

SCOPE = 'playlist-read-private playlist-modify-public app-remote-control playlist-modify-private user-modify-playback-state user-read-playback-state user-read-currently-playing'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=REDIRECT_URI,scope=SCOPE))
def listPlaylists():
    print("Your Playlists:")
    playlists = []
    offset = 0
    limit = 50 
    while True:
        results = sp.current_user_playlists(offset=offset, limit=limit)
        playlists.extend(results['items'])
        offset+=limit
        if len(results['items'])<limit:break
    for i, playlist in enumerate(playlists):
        print(f"{i + 1}. {playlist['name']}")
    return playlists


def getplayLists():
    playlists=[]
    offset=0
    limit=50 
    while True:
        results = sp.current_user_playlists(offset=offset, limit=limit)
        playlists.extend(results['items'])
        offset+=limit
        if len(results['items'])<limit:break
    return playlists

def clearShuffle(playlistNum):
    playlists = getplayLists()
    
    if 1<=playlistNum<=len(playlists):
        playlistselected=playlists[playlistNum-1]
        tracks=[]
        offset=0
        limit=100  
        while True:
            results = sp.playlist_tracks(playlistselected['id'],fields='items(track(name,uri))',offset=offset,limit=limit)
            tracks.extend(results['items'])
            offset+=limit
            if len(results['items'])<limit:break
        sp.start_playback(device_id=None, uris=[])
        random.shuffle(tracks)
        uris = [track['track']['uri'] for track in tracks]
        sp.start_playback(device_id=None, uris=uris)
        print(f"Playlist '{playlistselected['name']}' shuffled and added to the queue.")
    else:
        print("Invalid playlist number.")

if __name__ == "__main__":
    listPlaylists()
    playlistNum = int(input("Enter the number of the playlist you want to shuffle and add to the queue: "))
    clearShuffle(playlistNum)
