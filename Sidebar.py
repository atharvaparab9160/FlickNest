import pandas as pd
import pickle
import requests
import streamlit as st
from datetime import date
from streamlit_navigation_bar import st_navbar

##############################################
######## MOVIE RECOMMENDATION MODEL ##########
##############################################
from Recommendation_Model import get_cast
from Recommendation_Model import get_discription
from Recommendation_Model import get_poster_path
from Recommendation_Model import get_trending
from Recommendation_Model import recommend_similar_movie
from Recommendation_Model import get_general_recommendations
from Recommendation_Model import get_specific_genre_movie

from Recommendation_Model import similarity_matrix
from Recommendation_Model import movies_data


##############################################
######## MOVIE REVIEW SENTIMENT MODEL ########
##############################################
from Review_Sentiment_Analysis_Model import get_reviews
from Review_Sentiment_Analysis_Model import Review_sentiment

#############################################
########### MOVIE DETAILS ###################
#############################################
from Display_Movie_Discription import display_movie_details

#############################################
########### MOVIE GENRE ###################
#############################################
from Display_genre_movies import display_movie_of_genre

def Display_Sidebar():

    # Sample genres
    genres = ['Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
                             'Fantasy',
                             'Foreign', 'History', 'Horror', 'Music', 'Mystery', 'Romance', 'ScienceFiction', 'TVMovie',
                             'Thriller',
                             'War', 'Western']

    # Page configuration
    st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

    # Custom CSS for better sidebar design
    st.markdown(
        """
        <style>
        /* Sidebar style */
        .sidebar .sidebar-content {
            padding-top: 20px;
        }
        
        .genre-link {
            font-size: 18px;
            text-decoration: none;
            margin: 10px 0;
            display: block;
            padding: 8px;
            border-radius: 5px;
            transition: background-color 0.3s, color 0.3s;
        }
        .genre-link:hover {
            background-color: #f0f0f0;
            color: #1f77b4;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Sidebar with title, description, and styled genre links
    with st.sidebar:
        st.markdown("<h1>FlickNest</h1>", unsafe_allow_html=True)
        st.markdown("<h1><u>Explore by Genre</u></h1>", unsafe_allow_html=True)
        st.markdown("<h3>Find movies by selecting a genre below. Discover your next favorite film!</h3>", unsafe_allow_html=True)
        for genre in genres:
            st.markdown(f"<a class='genre-link' href='?genre_type={genre}'>{genre} Movies</a>", unsafe_allow_html=True)
