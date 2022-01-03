from find_songs import FindSongs
from spotify_api import Spotify

# 2010-08-11


def find_songs_add_playlist():
    user_input = input("Please type date in YYYY-MM-DD format: ")
    year = user_input.split("-")[0]

    find_songs = FindSongs(user_input=user_input)
    song_names = find_songs.song_names()

    spotify = Spotify(year=year)
    spotify.add_playlist(song_names=song_names)


if __name__ == "__main__":
    find_songs_add_playlist()
