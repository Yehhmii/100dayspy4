import requests
import lxml
from bs4 import BeautifulSoup


URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "lxml")

all_movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("movies.txt", "w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
