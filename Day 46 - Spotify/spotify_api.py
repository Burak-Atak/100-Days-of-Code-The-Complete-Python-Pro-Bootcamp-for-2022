import spotipy
from spotipy.oauth2 import SpotifyOAuth


Client_ID = "Your Client ID"
Client_Secret = "Client Secret"
playlist_id = "Your Playlist id"


class Spotify:
    # Acceces too spotify with api
    def __init__(self, year):
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope="playlist-modify-private",
                client_id=Client_ID,
                client_secret=Client_Secret,
                redirect_uri="https://example.com/",
                show_dialog=True,
                cache_path="token.txt"
            )
        )
        self.year = year
        self.user_id = self.sp.current_user()["id"]
    
    # Add a list of songs to a spotify playlist.
    def add_playlist(self, song_names):
        songs_id = []
        for song in song_names:
            song = song.split("\n")[1]

            result = self.sp.search(f"track:{song} year:{self.year}", type="track")
            try:
                song_id = result["tracks"]["items"][0]["id"]
                songs_id.append(song_id)
            except IndexError:
                print(f"{song} doesn't exist in Spotify. Skipped.")
            
        self.sp.playlist_add_items(playlist_id=playlist_id, items=songs_id)
