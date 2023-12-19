import requests
import os
from dotenv import load_dotenv

# Load environment variables from the api.env file
load_dotenv(dotenv_path="api.env")

# Access the API key
api_key = os.getenv("API_KEY")


def fetch_poster(movie_id):
   response = requests.get(
       f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}')
   data = response.json()
   return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
