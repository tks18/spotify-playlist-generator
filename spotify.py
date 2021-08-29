import spotipy
from spotipy.oauth2 import SpotifyOAuth


class spotify:
    def __init__(self, client_id, client_secret, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.client = self.connect_user()

    def connect_user(self):
        scope = "user-library-read,playlist-modify-private,playlist-modify-public"
        client = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=self.client_id,
                client_secret=self.client_secret,
                redirect_uri=self.redirect_uri,
                scope=scope,
                show_dialog=True,
                cache_path="token.txt",
            )
        )
        return client

    def user_details(self):
        user = self.client.current_user()
        self.user = user
        return user

    def create_playlist(self, name, description, public=True):
        playlist = self.client.user_playlist_create(
            user=self.user["id"],
            name=name,
            public=public,
            collaborative=False,
            description=description,
        )
        return playlist

    def find_song(self, song_name, year=None):
        if year is not None:
            song_search = self.client.search(
                q=f"track: {song_name} year: {year}", limit=1, type="track"
            )
        else:
            song_search = self.client.search(
                q="track: {song_name}", limit=1, type="track"
            )

        try:
            song_info = song_search["tracks"]["items"][0]["uri"]
            if song_info:
                return song_search["tracks"]["items"][0]
            else:
                False
        except:
            return False
