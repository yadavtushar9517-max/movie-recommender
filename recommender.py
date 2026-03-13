import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# load dataset
movies = pd.read_csv("movies.csv")

# fill missing genres
movies['genres'] = movies['genres'].fillna('')

# convert genres into numerical vectors
cv = CountVectorizer(tokenizer=lambda x: x.split('|'))

genre_matrix = cv.fit_transform(movies['genres'])

# compute similarity
similarity = cosine_similarity(genre_matrix)

# recommendation function
def recommend(movie_name):

    movie_index = movies[movies['title'] == movie_name].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:10]

    recommendations = []

    for i in movie_list:
        recommendations.append(movies.iloc[i[0]].title)

    return recommendations
