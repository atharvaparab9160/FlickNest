import pandas as pd
import pickle
import requests
import streamlit as st
# st.set_page_config(page_title="FlickNest",layout="centered", initial_sidebar_state="collapsed")
st.set_page_config(page_title="FlickNest",layout="centered", initial_sidebar_state="auto")
from datetime import date
from streamlit_navigation_bar import st_navbar
from streamlit_option_menu import option_menu

from Display_genre_movies import display_movie_of_genre


##############################################
######## MOVIE RECOMMENDATION MODEL ##########
##############################################
import Home
#
#
# ##############################################
# ######## MOVIE RECOMMENDATION MODEL ##########
# ##############################################
# from Recommendation_Model import get_cast
# from Recommendation_Model import get_discription
# from Recommendation_Model import get_poster_path
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

#############################################
########### Login/SignUp Page ###################
#############################################
import User_Login_Signup

#############################################
########### Special_Recommendation ###################
#############################################

import Special_Recommendation


def Display_Sidebar():
    ...

# st.set_page_config(
#     page_title="FlickNest"
# )
# st.set_page_config(page_title="FlickNest",layout="centered", initial_sidebar_state="collapsed")
# remove watermark
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run(self):

        with st.sidebar:
            apps_op  = option_menu(
                menu_title='FlickNest',
                options=['Home', 'Account','---','For You','---','Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
                      'Fantasy','Foreign', 'History', 'Horror', 'Music', 'Mystery', 'Romance', 'ScienceFiction', 'TVMovie',
                      'Thriller','War', 'Western'],
                icons=['house-fill', 'person-circle' , "award-fill" , "award-fill" ],
                menu_icon='film',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px" },
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "5px",
                                 "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"}, }
            )


            # genres = ['Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
            #           'Fantasy',
            #           'Foreign', 'History', 'Horror', 'Music', 'Mystery', 'Romance', 'ScienceFiction', 'TVMovie',
            #           'Thriller',
            #           'War', 'Western']



            # Custom CSS for better sidebar design
            # st.markdown(
            #     """
            #     <style>
            #     /* Sidebar style */
            #     .sidebar .sidebar-content {
            #         padding-top: 20px;
            #     }
            #
            #     .genre-link {
            #         font-size: 18px;
            #         text-decoration: none;
            #         margin: 10px 0;
            #         display: block;
            #         padding: 8px;
            #         border-radius: 5px;
            #         transition: background-color 0.3s, color 0.3s;
            #     }
            #     .genre-link:hover {
            #         background-color: #f0f0f0;
            #         color: #1f77b4;
            #     }
            #     </style>
            #     """,
            #     unsafe_allow_html=True
            # )

            # Sidebar with title, description, and styled genre links
            # with st.sidebar:
            # st.markdown("<h1>FlickNest</h1>", unsafe_allow_html=True)
            # st.markdown("<h1><u>Explore by Genre</u></h1>", unsafe_allow_html=True)
            # st.markdown("<h3>Find movies by selecting a genre below. Discover your next favorite film!</h3>",
            #                 unsafe_allow_html=True)
            # for genre in genres:
            #     st.markdown(f"<a class='genre-link' href='?genre_type={genre}'>{genre} Movies</a>",
            #                     unsafe_allow_html=True)
        genresList = ['Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
                      'Fantasy','Foreign', 'History', 'Horror', 'Music', 'Mystery', 'Romance', 'ScienceFiction', 'TVMovie',
                      'Thriller','War', 'Western']
        # st.write(SelectedGenere)

        if apps_op == "Home":
            Home.app()
        elif apps_op == "Account":
            User_Login_Signup.app()
        elif apps_op == "For You":
            Special_Recommendation.app()
        elif apps_op in genresList:
            display_movie_of_genre(apps_op)


RunObj = MultiApp()
RunObj.run()


    # Sample genres
    # genres = ['Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
    #                          'Fantasy',
    #                          'Foreign', 'History', 'Horror', 'Music', 'Mystery', 'Romance', 'ScienceFiction', 'TVMovie',
    #                          'Thriller',
    #                          'War', 'Western']
    #
    # # Page configuration
    # st.set_page_config(layout="centered", initial_sidebar_state="collapsed")
    #
    #
    # # Custom CSS for better sidebar design
    # st.markdown(
    #     """
    #     <style>
    #     /* Sidebar style */
    #     .sidebar .sidebar-content {
    #         padding-top: 20px;
    #     }
    #
    #     .genre-link {
    #         font-size: 18px;
    #         text-decoration: none;
    #         margin: 10px 0;
    #         display: block;
    #         padding: 8px;
    #         border-radius: 5px;
    #         transition: background-color 0.3s, color 0.3s;
    #     }
    #     .genre-link:hover {
    #         background-color: #f0f0f0;
    #         color: #1f77b4;
    #     }
    #     </style>
    #     """,
    #     unsafe_allow_html=True
    # )
    #
    # # Sidebar with title, description, and styled genre links
    # with st.sidebar:
    #     st.markdown("<h1>FlickNest</h1>", unsafe_allow_html=True)
    #     st.markdown("<h1><u>Explore by Genre</u></h1>", unsafe_allow_html=True)
    #     st.markdown("<h3>Find movies by selecting a genre below. Discover your next favorite film!</h3>", unsafe_allow_html=True)
    #     for genre in genres:
    #         st.markdown(f"<a class='genre-link' href='?genre_type={genre}'>{genre} Movies</a>", unsafe_allow_html=True)
    #

