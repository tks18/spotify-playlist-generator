from dotenv import load_dotenv
from spotify import spotify
from handlers import handle_txt
from os import getenv

load_dotenv()

CLIENT_ID = getenv("CLIENT_ID")
CLIENT_SECRET = getenv("CLIENT_SECRET")
REDIRECT_URI = getenv("REDIRECT_URI")

spotify_client = spotify(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI
)

spotify_client.user_details()

tracklist = handle_txt("tracklist.txt")

spotify_track_objs = []

for tracks in tracklist:
    song = spotify_client.find_song(song_name=tracks["title"], artist=tracks["artist"])
    if song:
        spotify_track_objs.append(song["uri"])
    else:
        print(f"{tracks['title']} by {tracks['artist']} Not Found")

if len(spotify_track_objs) == len(tracklist):
    print("All Songs Found")
else:
    print(f"{len(spotify_track_objs)}/{len(tracklist)} Songs Found")

if len(spotify_track_objs) > 2:
    print("Creating Playlist")
    name = input("Enter the Playlist Name: (Use Case) ")
    description = input("Enter a Description for Playlist: ")

    spty_playlist = spotify_client.create_playlist(name=name, description=description)
    spotify_client.add_to_playlist(playlist=spty_playlist, songs=spotify_track_objs)
