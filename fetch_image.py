import requests

def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=c4ed22a0b609ff0085b68628115997b9'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
