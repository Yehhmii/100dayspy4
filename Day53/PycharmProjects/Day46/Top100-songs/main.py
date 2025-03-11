import requests
import lxml
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

SPOTIFY_CLIENT_ID = os.environ.get("CLIENT_ID")
SPOTIFY_AUTH = os.environ.get("AUTH")
UNAME = os.environ.get("USERNAME")

# Scraping Billboard 100
date = input("Which your do you want to travel to? Type the date in the format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(URL)
billboard_html = response.text

soup = BeautifulSoup(billboard_html, "lxml")
all_song = soup.select("li ul li h3")
all_song_title = [song_title.getText().strip() for song_title in all_song]


# authenticating out spotify api
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_AUTH,
        show_dialog=True,
        cache_path="token.txt",
        username=UNAME
    )
)
user_id = sp.current_user()["id"]
print(user_id)

# Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in all_song_title:
    result = sp.search(
        q=f"track:{song} year:{year}", type="track"
    )
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
