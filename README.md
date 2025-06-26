
# 🎬 Movie Recommendation System

A simple content-based movie recommendation system built with Python, Streamlit, and Pickle. The system recommends similar movies based on the input movie title using a similarity matrix.


## 📂 Project Structure
.
├── main.py                # Streamlit app script
├── movies.pkl             # Preprocessed movie metadata
├── similarity.pkl         # Precomputed cosine similarity matrix
├── movie_recommendation.ipynb  # Jupyter notebook (development and testing)

## Features

1.User-friendly Streamlit UI

2.Recommends top 5 similar movies based on title

3.Handles punctuation and input variations gracefully

4.Uses difflib for approximate string matching

5.Displays user-friendly messages for invalid or unmatched input
## 🛠️ Tech Stack
Python

Streamlit

Pandas

Pickle

difflib


## ❗ Notes
1. Input matching is case-insensitive and ignores punctuation.

2. Input must closely match an existing movie title in movies.pkl.
   

## Sample output


Enter the movie title: Inception

Top 5 Similar Movies:
1. Inception
2. The Dark Knight
3. Memento
4. The Prestige
5. Tenet



