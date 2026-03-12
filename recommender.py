import pandas as pd

movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

data = pd.merge(ratings, movies, on="movieId")

# filter popular movies
movie_counts = data['title'].value_counts()
popular_movies = movie_counts[movie_counts > 50].index
data = data[data['title'].isin(popular_movies)]

# pivot table
user_movie_matrix = data.pivot_table(
    index='userId',
    columns='title',
    values='rating'
)

def recommend(movie_name):

    movie_ratings = user_movie_matrix[movie_name]

    similar_movies = user_movie_matrix.corrwith(movie_ratings)

    corr_df = pd.DataFrame(similar_movies, columns=['correlation'])

    corr_df.dropna(inplace=True)

    recommendations = corr_df.sort_values(
        'correlation', ascending=False
    ).head(10)

    return recommendations.index.tolist()