from datetime import datetime
from billboard import Billboard
from spotify import Spotify

from dotenv import load_dotenv
import os

load_dotenv("../.env")

SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
SPOTIPY_USERNAME = os.environ.get("SPOTIPY_USERNAME")

date = None
date_format = "%Y-%m-%d"
while not date:
    try:
        user_text_input = input(f"Which yeaf do you want to travel to ? type the date in this format YYYY-MM-DD: ")
        date = datetime.strptime(user_text_input, date_format)
    except ValueError:
        pass
billboard = Billboard()
songs = billboard.getTop100(date)

sp = Spotify(username=SPOTIPY_USERNAME, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
for song in songs:
    result = sp.getPreview(f"{song['artist']} {song['title']}")
    preview_uri = result['tracks']['items'][0]['preview_url']
    if preview_uri:
        print(preview_uri)