from dotenv import load_dotenv
from spotify import spotify
from os import getenv

load_dotenv()

CLIENT_ID = getenv("CLIENT_ID")
CLIENT_SECRET = getenv("CLIENT_SECRET")
REDIRECT_URI = getenv("REDIRECT_URI")

spotify_client = spotify(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI
)

spotify_client.user_details()

song = spotify_client.find_song(song_name="Skate", year="2021")
print(song)