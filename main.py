import streamlit as st
import pickle
import pandas as pd
import difflib
import string

with open("movies.pkl","rb")as f:
    movies = pickle.load(f)
with open("similarity.pkl","rb") as f:
    similarity = pickle.load(f)  

def recommend(movies_title):
    translator = str.maketrans("","", string.punctuation)

    title = movies['original_title'].str.lower()
    cleaned_title = title.str.translate(translator)
    cleaned_input = movies_title.lower().translate(translator)

    mactches = difflib.get_close_matches(cleaned_input, cleaned_title, n=2, cutoff=0.4)

    if not mactches:
        st.error(f"{movies_title} not found")
        return
    
    best_match = mactches[0]
    movie_index = cleaned_title[cleaned_title == best_match].index[0]
    movie_list = sorted(list(enumerate(similarity[movie_index])),
                        key = lambda x : x[1],
                        reverse=True)
    

    finded_movies = []
    for movie in movie_list[1:6]:
        finded_movies.append(movies.iloc[movie[0]]['original_title'])
    
    return finded_movies


st.title("🎬 Movie Recommendation System")

movie_input = st.text_input("Enter the movie title")
if st.button("Get Recommendation"):

    if movie_input is None:
        st.warning("No input detected")
    if movie_input.strip() == "":
        st.warning("Enter the valid input")
    else:
        results = recommend(movie_input)
        if results is None:
            st.error("No recommendations found")
            st.stop()
        st.subheader("Top 5 Similar Movies")
        for i , movie in enumerate(results, 1):
            st.write(f"{i}.{movie}")

