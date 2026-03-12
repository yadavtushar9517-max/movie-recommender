import streamlit as st
from recommender import recommend, user_movie_matrix

st.title("🎬 Movie Recommendation System")

st.write("Select a movie to get recommendations")

movie_list = user_movie_matrix.columns.tolist()

selected_movie = st.selectbox(
    "Choose a movie",
    movie_list
)

if st.button("Recommend"):

    recommendations = recommend(selected_movie)

    st.subheader("Recommended Movies")

    for movie in recommendations:
        st.write(movie)