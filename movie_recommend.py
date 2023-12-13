import os
import pickle
import pandas as pd
from fetch_image import fetch_poster

# Get the absolute path of the script's directory
script_directory = os.path.dirname(os.path.abspath(__file__))

# Specify absolute paths for the pickle files
movies_dict_path = os.path.join(script_directory, 'movies_dict.pkl')
similarity_path = os.path.join(script_directory, 'similarity.pkl')

movies_dict = pickle.load(open(movies_dict_path, 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open(similarity_path, 'rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),
                         reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
       recommended_movies.append(movies.iloc[i[0]].title)
       # Fetch movie poster from TMDB API
       recommended_movies_posters.append(
           fetch_poster(movies.iloc[i[0]].movie_id))
    return recommended_movies, recommended_movies_posters