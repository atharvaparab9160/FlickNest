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
# from Recommendation_Model import get_trending
# from Recommendation_Model import recommend_similar_movie
# from Recommendation_Model import get_general_recommendations
# from Recommendation_Model import get_specific_genre_movie
#
# from Recommendation_Model import similarity_matrix
# from Recommendation_Model import movies_data
#
#
# ##############################################
# ######## MOVIE REVIEW SENTIMENT MODEL ########
# ##############################################
# from Review_Sentiment_Analysis_Model import get_reviews
# from Review_Sentiment_Analysis_Model import Review_sentiment
#
# #############################################
# ########### MOVIE DETAILS ###################
# #############################################
# from Display_Movie_Discription import display_movie_details
#
# #############################################
# ########### MOVIE GENRE ###################
# #############################################
# from Display_genre_movies import display_movie_of_genre

import streamlit as st


def display_navbar():
    ...


