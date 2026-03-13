import streamlit as st
import pandas as pd
from recommender import recommend

st.title("🎬 Movie Recommendation System")
movies=pd.read_csv("movies.csv")

st.write("Select a movie to get recommendations")

movie_list = movies["title"].tolist()

selected_movie = st.selectbox(
    "Choose a movie",
    movie_list
)

if st.button("Recommend"):

    recommendations = recommend(selected_movie)

    st.subheader("Recommended Movies")

    for movie in recommendations:

        st.write(movie)
