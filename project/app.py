import streamlit as st
import pickle
import pandas as pd


movies_list = pickle.load(open('movies_list.pkl', 'rb'))
similarity = pickle.load(open('similarity_matrix.pkl', 'rb'))
print(movies_list)
print(type(movies_list))

movies = pd.DataFrame(movies_list)

def recommend(movie_name):
    if movie_name not in movies['movie_name'].values:
        return ["Movie not found!"]
    index = movies[movies['movie_name'] == movie_name].index[0]
    distances = similarity[index]
    movie_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = [movies.iloc[i[0]]['movie_name'] for i in movie_indices]  # Fixed column name
    return recommended_movies

# Streamlit UI
st.title('Movie Recommender System')

# Auto-complete dropdown with typing
movie_name = st.selectbox(
    'Type or select a movie from the dropdown:',
    movies['movie_name'].values
)

if st.button('Recommend'):
    recommendations = recommend(movie_name)
    st.subheader('Recommended Movies:')
    for i, movie in enumerate(recommendations, 1):
        st.write(f"{i}. {movie}")
