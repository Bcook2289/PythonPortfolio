import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
hm_webpage = response.text

soup = BeautifulSoup(hm_webpage, "html.parser")
movies = soup.find_all(name="h3", class_="title")
movie_title = []
for title in movies:
    movie_title.append(title.getText())
movie_title = movie_title[::-1]
with open("movies.txt", "w", encoding="utf-8") as file:
    for t in movie_title:
        file.write(t)
        file.write("\n")

