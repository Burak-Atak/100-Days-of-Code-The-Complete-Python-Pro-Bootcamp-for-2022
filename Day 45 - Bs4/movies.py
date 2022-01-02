import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text, "html.parser")

names = soup.find_all(name="h3", class_="title")

text = open("movies.txt", "w")
for tag in names[::-1]:
    movie_name = tag.getText()
    text.write(f"{movie_name}\n")
text.close()


