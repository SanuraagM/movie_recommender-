import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=e2dcced7e664c7dab82e4381e0b42090&language=en-US'.format(movie_id))
    data = response.json()
    print(data)
    return 'https://image.tmdb.org/t/p/w500' + data['poster_path']

def recommend(movie):
      movie_index = df[df['title']==movie].index[0]
      distance = similarity[movie_index]
      movies_list = sorted(list(enumerate(distance)),reverse = True , key = lambda x:x[1])[1:6]

      recommended_movies = []
      recommended_movies_posters = []
      for i in movies_list:
        movie_id = df.iloc[i[0]].movie_id
        recommended_movies.append(df.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
      return recommended_movies,recommended_movies_posters


df = pickle.load(open('movies.pkl',"rb"))
movies = df['title'].values

similarity = pickle.load(open('similarity.pkl',"rb"))

st.title('Movie Recommender system')

selected_movie = st.selectbox(
    "How would you like to be contacted?",
    movies,
)

st.write("You selected:", selected_movie)

if st.button('Recommend'):
    names,posters = recommend(selected_movie)

    col1,col2,col3,col4,col5 = st.columns(5)
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
