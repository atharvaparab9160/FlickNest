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



def display_movie_of_genre(genre):
    ##############################################
    ######## DISPLAY MOVIE PART ##################
    ##############################################
    st.markdown(f"<h1>Recommending {genre} Movies🔎</h1>", unsafe_allow_html=True)
    with st.spinner('Finding the perfect movies just for you...Sit tight!'):
        total_recommend_movies = 24

        movies = get_specific_genre_movie(genre,total_recommend_movies)
        st.markdown(
            """
            <style>
            .clickable-image {
                cursor: pointer;
            }
            .clickable-image:hover {
                transform: scale(1.05);
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        for i in range(0, min(len(movies),total_recommend_movies), 4):

            col1, col2, col3, col4 = st.columns(4, gap="medium", vertical_alignment="center")
            if i < total_recommend_movies:
                with col1:
                    image_html = f"""
                                                <a href="?movie_id={movies[i][0]}">
                                                    <img src="{movies[i][2]}" style="width: 13vw;" class="clickable-image"/>
                                                </a>
                                                """
                    st.markdown(image_html, unsafe_allow_html=True)
                    st.text(movies[i][1])
            if i + 1 < total_recommend_movies:
                with col2:
                    image_html = f"""
                                                            <a href="?movie_id={movies[i + 1][0]}">
                                                                <img src="{movies[i + 1][2]}" style="width: 13vw;" class="clickable-image"/>
                                                            </a>
                                                            """
                    st.markdown(image_html, unsafe_allow_html=True)
                    st.text(movies[i + 1][1])
            if i + 2 < total_recommend_movies:
                with col3:
                    image_html = f"""
                                                            <a href="?movie_id={movies[i + 2][0]}">
                                                                <img src="{movies[i + 2][2]}" style="width: 13vw;" class="clickable-image"/>
                                                            </a>
                                                            """
                    st.markdown(image_html, unsafe_allow_html=True)
                    st.text(movies[i + 2][1])
            if i + 3 < total_recommend_movies:
                with col4:
                    image_html = f"""
                                                            <a href="?movie_id={movies[i + 3][0]}">
                                                                <img src="{movies[i + 3][2]}" style="width: 13vw;" class="clickable-image"/>
                                                            </a>
                                                            """
                    st.markdown(image_html, unsafe_allow_html=True)
                    st.text(movies[i + 3][1])
            # if i + 4 < total_recommend_movies:
            #     with col5:
            #         image_html = f"""
            #                                                 <a href="?movie_id={movies[i + 4][0]}">
            #                                                     <img src="{movies[i + 4][2]}" style="width: 13vw;" class="clickable-image"/>
            #                                                 </a>
            #                                                 """
            #         st.markdown(image_html, unsafe_allow_html=True)
            #         st.text(movies[i + 4][1])