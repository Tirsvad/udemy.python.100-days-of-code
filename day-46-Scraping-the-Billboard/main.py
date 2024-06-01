import datetime
import os

import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

URL = "https://www.billboard.com/charts/hot-100"

# sp = spotipy.Spotify(
#     auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,
#                                           client_secret=CLIENT_SECRET))


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private",
                                               show_dialog=True
                                               ))


def validate_date_format(date) -> bool:
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d").strftime('%Y-%m-%d')
    except ValueError:
        print("Date format have to be YYYY-MM-DD")
        return False
    else:
        return True


date = "2020-02-02"
while not validate_date_format(date):
    date = input("Which date to find top 100 music YYYY-MM-DD?")

api = f"{URL}/{date}"

response = requests.get(url=api)
response.raise_for_status()

content = response.text

soup = BeautifulSoup(markup=content, features="html.parser")
song_names_container = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_container]

song_uris = []
year = date.split("-")[0]

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

user_id = sp.current_user()["id"]
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
