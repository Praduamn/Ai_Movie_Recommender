import streamlit as st
import pandas as pd
import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


@st.cache_resource
def load_data():
    movies = pd.read_csv("tmdb_5000_movies.csv")
    credits = pd.read_csv("tmdb_5000_credits.csv")
    movies = movies.merge(credits, on="title")

    # Helper functions
    def convert(text):
        return [i['name'] for i in ast.literal_eval(text)]

    def convert3(text):
        L, counter = [], 0
        for i in ast.literal_eval(text):
            if counter != 3:
                L.append(i['name'])
                counter += 1
            else:
                break
        return L

    def fetch_director(text):
        for i in ast.literal_eval(text):
            if i['job'] == 'Director':
                return [i['name']]
        return []

    # Keep useful columns
    movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
    movies.dropna(inplace=True)

    # Apply transformations
    movies['genres'] = movies['genres'].apply(convert)
    movies['keywords'] = movies['keywords'].apply(convert)
    movies['cast'] = movies['cast'].apply(convert3)
    movies['crew'] = movies['crew'].apply(fetch_director)

    movies['overview'] = movies['overview'].apply(lambda x: x.split())
    movies['genres'] = movies['genres'].apply(lambda x: [i.replace(" ", "") for i in x])
    movies['keywords'] = movies['keywords'].apply(lambda x: [i.replace(" ", "") for i in x])
    movies['cast'] = movies['cast'].apply(lambda x: [i.replace(" ", "") for i in x])
    movies['crew'] = movies['crew'].apply(lambda x: [i.replace(" ", "") for i in x])

    # Combine into tags
    movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']
    new = movies[['movie_id', 'title', 'tags', 'genres', 'cast', 'crew']]
    new['tags'] = new['tags'].apply(lambda x: " ".join(x).lower())

    # Vectorization + similarity
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(new['tags']).toarray()
    similarity = cosine_similarity(vectors)

    return new, similarity


movies, similarity = load_data()


# ----------------- Recommendation Functions -----------------
def recommend(movie):
    movie = movie.lower()
    if movie not in movies['title'].str.lower().values:
        return ["Movie not found in dataset."]
    index = movies[movies['title'].str.lower() == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [movies.iloc[i[0]].title for i in movies_list]


def recommend_by_genre(genre):
    matched = movies[movies['genres'].apply(lambda x: genre.lower() in [g.lower() for g in x])]
    return matched['title'].sample(n=min(5, len(matched)), replace=False).tolist() if not matched.empty else ["No movies found."]


def recommend_by_actor(actor):
    matched = movies[movies['cast'].apply(lambda x: actor.lower() in [a.lower() for a in x])]
    return matched['title'].sample(n=min(5, len(matched)), replace=False).tolist() if not matched.empty else ["No movies found."]


def recommend_by_director(director):
    matched = movies[movies['crew'].apply(lambda x: director.lower() in [d.lower() for d in x])]
    return matched['title'].sample(n=min(5, len(matched)), replace=False).tolist() if not matched.empty else ["No movies found."]


# ----------------- Streamlit UI -----------------
st.title("🎬 Movie Recommendation System")

# Sidebar choice
st.sidebar.title("🔍 Search Options")
search_mode = st.sidebar.radio("Search by:", ["Movie (Default)", "Genre", "Actor", "Director"], index=0)

# Movie Recommendation (default)
if search_mode == "Movie (Default)":
    selected_movie = st.selectbox("🎥 Type or select a movie", movies['title'].values)
    if st.button("Recommend"):
        recommendations = recommend(selected_movie)
        st.write("### ✅ Recommended Movies:")
        for i in recommendations:
            st.write(i)

# Genre Recommendation
elif search_mode == "Genre":
    all_genres = sorted(set([g for sublist in movies['genres'] for g in sublist]))
    selected_genre = st.selectbox("🎭 Choose a genre", all_genres)
    if st.button("Show Genre Recommendations"):
        recommendations = recommend_by_genre(selected_genre)
        st.write(f"### 🎭 Movies in {selected_genre}:")
        for i in recommendations:
            st.write(i)

# Actor Recommendation
elif search_mode == "Actor":
    all_actors = sorted(set([a for sublist in movies['cast'] for a in sublist]))
    selected_actor = st.selectbox("⭐ Choose an actor", all_actors)
    if st.button("Show Actor Recommendations"):
        recommendations = recommend_by_actor(selected_actor)
        st.write(f"### ⭐ Movies with {selected_actor}:")
        for i in recommendations:
            st.write(i)

# Director Recommendation
elif search_mode == "Director":
    all_directors = sorted(set([d for sublist in movies['crew'] for d in sublist]))
    selected_director = st.selectbox("🎬 Choose a director", all_directors)
    if st.button("Show Director Recommendations"):
        recommendations = recommend_by_director(selected_director)
        st.write(f"### 🎬 Movies directed by {selected_director}:")
        for i in recommendations:
            st.write(i)
