import streamlit as st
import pickle  # For loading data from pickle files
import pandas as pd
import os
# to import a functiom from another file, use the following syntax: from file_name import function_name
from movie_recommend import recommend

# # Get the absolute path of the script's directory
script_directory = os.path.dirname(os.path.abspath(__file__))

# # Specify absolute paths for the pickle files
movies_dict_path = os.path.join(script_directory, 'movies_dict.pkl')

# Function to recommend movies based on user input
# Load movie data and similarity matrix
movies_dict = pickle.load(open(movies_dict_path, 'rb'))
movies = pd.DataFrame(movies_dict)

# Streamlit app title
st.title('Movie Recommended System')

# User input for movie selection
selected_movie_name = st.selectbox(
    'Please Search the Movie', movies['title'].values)

# Recommendation button
if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
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
