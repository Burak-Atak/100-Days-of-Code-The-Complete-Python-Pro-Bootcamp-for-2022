from bs4 import BeautifulSoup
import requests

# with open("website.html", encoding="utf8") as web:
#     content = web.read()

# soup = BeautifulSoup(content, "html.parser")
# print(soup.title) komple bütün ögeyi alır
# print(soup.title.name) direk tagın ismini alır
# print(soup.title.string) tag ögesinin içindeki metini alır
# print(soup.prettify()) düzgün yazar
# print(soup.ul) taga göre aratır ilk aynı taglıyı alıor

# all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
    # print(tag.getText()) tagların metnini döndürür
    # print(tag.get("href")) taglardak href ögesinin içini döndürür

# heading = soup.find(name="h1", id="name")
# section_heading = soup.find(name="h3", class_="heading") # class_ yapmak lazım seçebilemk için

response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, "html.parser")
anchors = soup.find_all(name="a", class_="titlelink")
scores = soup.find_all(name="span", class_="score")

anchors.pop(15)

scores_list = []
tag_texts = []
links = []

num = 0
for tag in anchors:
    score = int(scores[num].getText().split(" ")[0])
    scores_list.append(score)
    tag_texts.append(tag.getText())
    link = tag.get("href")
    links.append(link)

    num += 1

maximum = max(scores_list)
index = scores_list.index(maximum)
print(anchors[-1])
print(tag_texts[index] + "\n" + links[index] + "\n" + str(scores_list[index]))