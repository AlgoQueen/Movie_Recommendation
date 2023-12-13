import streamlit as st
import pickle # For loading data from pickle files
# use of pickle over text files is that it is faster and more efficient
# pickle file is a binary file that stores a Python object in serialized format 
# why dump data into pickle file?
# 1. to save the data for later use, 2. to send data over a network connection, 3. to store data in a database, 4. to convert an object to a string, 5. to convert an object to a byte stream, 6. to maintain object state across sessions, 7. to send python data from one script to another, 8. to store python objects in a file or database
import pandas as pd
import os
import requests
     
# Get the absolute path of the script's directory
script_directory = os.path.dirname(os.path.abspath(__file__))

# Specify absolute paths for the pickle files
movies_dict_path = os.path.join(script_directory, 'movies_dict.pkl')
similarity_path = os.path.join(script_directory, 'similarity.pkl')

# Load data from pickle files
# movies_dict = pickle.load(open(movies_dict_path, 'rb'))
# movies_dict = pickle.load(open(file_path, 'rb'))

# Function to recommend movies based on user input
# Load movie data and similarity matrix
movies_dict = pickle.load(open(movies_dict_path, 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open(similarity_path, 'rb'))


def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=c4ed22a0b609ff0085b68628115997b9'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
       recommended_movies.append(movies.iloc[i[0]].title)
       # Fetch movie poster from TMDB API
       recommended_movies_posters.append(fetch_poster(movies.iloc[i[0]].movie_id))
    return recommended_movies,recommended_movies_posters

# Streamlit app title
st.title('Movie Recommended System')

# User input for movie selection
selected_movie_name = st.selectbox('Please Search the Movie', movies['title'].values)

# Recommendation button
if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
  
