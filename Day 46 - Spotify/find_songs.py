import requests
from bs4 import BeautifulSoup


class FindSongs:
    # Find popular songs in a spesifiic date return song names
    def __init__(self, user_input: str):
        self.url = f"https://www.billboard.com/charts/hot-100/{user_input}/"
        self.response = requests.get(self.url)
        self.soup = BeautifulSoup(self.response.text, "html.parser")

    def song_names(self):
        song_name_tags = self.soup.find_all(name="h3", id="title-of-a-story", class_="c-title")

        while True:
            for tag in song_name_tags:
                if len(tag.get("class")) <= 5:
                    song_name_tags.remove(tag)
            if len(song_name_tags) <= 101:
                song_name_tags.pop(-1)
                break

        song_names = [tag.getText() for tag in song_name_tags]

        return song_names
