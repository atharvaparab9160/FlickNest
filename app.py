import pandas as pd
import pickle
import requests
import streamlit as st
import time
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
########### SIDEBAR  ########################
#############################################
from Sidebar import Display_Sidebar
#############################################
###########  NAVBAR  ########################
#############################################
from Navbar import display_navbar

#############################################
########### MOVIE BY GENRE ###################
#############################################
from Display_genre_movies import display_movie_of_genre


##############################################
############## MOVIE SLIDER ##################
##############################################

def Movie_Slider():
    no_of_movies = 7
    trending_Movie  = get_trending(no_of_movies)
    carousel_boot_link = '''
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.3.0/font/bootstrap-icons.css" rel="stylesheet" />
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz"
            crossorigin="anonymous"></script>

    <style>
    #slider {
        position: absolute;
    }

    .title {
        size: 5rem;
    }

    .rating {
        size: 1rem;
    }

    .slider-image { 
        /* position: absolute; */

        z-index: -1;
        height: 100vh;
        width: 100vw;
        # opacity: 0.5;

     }

    #slider-info {
            width: 100vw;
            position: absolute;
            top: 55%;
            left: 50%;
            transform: translate(-50%, 13%);
            color: white;
            font-size: 24px;
            # font-weight: bold; 
            text-align: left;
            background-color: rgba(0, 0, 0, 0.5); 
            padding: 10px;
        /* white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        max-width: 48%; */

    }
    .info-title{
        display: inline-block;
        font-weight: bold;
        font-size: 2rem;

        width: 95vw; /* Adjust the width as per your requirements */
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    .info-rating{
        font-weight:600;
        font-size: 1.3rem;
    }
    .info-genre{
        font-size: 1.8rem;
        color: rgba(157, 157, 157, 1);
        # font-weight:bold;
    }
    .info-overview{
        display: -webkit-box;
        -webkit-line-clamp: 2; /* Number of lines to show */
        -webkit-box-orient: vertical;
        /* white-space: nowrap; */
        overflow: hidden;
        text-overflow: ellipsis;
        max-width: 100%;
        font-size: 0.9rem;
    }
    @media screen and (min-width: 0px) and (max-width:296px){
        #slider-info{
            top: 65%;
        }
    }
    </style>        

    '''
    carousel_start = '''
    <div id="carouselExampleRide" class="carousel slide carousel-fade" data-ride="carousel" data-bs-ride="true">
    <div class="carousel-inner">
    '''
    carousel_end = '''
        </div>
            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleRide" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span> 
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleRide" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
            </button>
        </div>

    '''
    Full_html = ""
    Full_html += carousel_boot_link
    Full_html += carousel_start

    for i in range(no_of_movies):
        title = trending_Movie[i][0]
        genre = trending_Movie[i][1]
        image_path = trending_Movie[i][2]
        overview = trending_Movie[i][3]
        rating = trending_Movie[i][4]
        m_id = trending_Movie[i][5]
        if i == 0:
            carousel_top_sliders = f'''
                <div class="carousel-item active">
                    <a href="?movie_id={m_id}" target="_blank">
                    <img class="slider-image" src="{image_path}" alt="...">
                    </a>
                    <div id="slider-info">
                        <span class="info-title">{title}</span><br>
                        <span class="info-rating">Ratings : {rating}</span><br>
                        <span class="info-genre">{genre}</span><br>
                        <span class="info-overview">{overview}</span>
                    </div>
                    
                </div>
                '''
            Full_html += carousel_top_sliders
        else:
            carousel_sliders = f'''
                <div class="carousel-item">
                    <a href="?movie_id={m_id}" target="_blank">
                    <img class="slider-image" src="{image_path}" alt="...">
                    </a>
                    <div id="slider-info">
                        <span class="info-title">{title}</span><br>
                        <span class="info-rating">Ratings : {rating}</span><br>
                        <span class="info-genre">{genre}</span><br>
                        <span class="info-overview">{overview}</span>
                    </div>
                </div>
                '''
            Full_html += carousel_sliders


    Full_html += carousel_end
    st.components.v1.html(Full_html, height=500)




# START START START START START START START START START START START START START START START START START START START START START
# START START START START START START START START START START START START START START START START START START START START START START



query_params = st.query_params
if 'selected_movie' not in st.session_state:
    st.session_state['selected_movie'] = None
if 'selected_genre' not in st.session_state:
    st.session_state['selected_genre'] = None

if 'movie_id' in query_params:
    st.session_state['selected_movie'] = int(query_params['movie_id'])
if 'genre_type' in query_params:
    st.session_state['selected_genre'] = query_params['genre_type']

#
# side bar
#
Display_Sidebar()
st.title("FlickNest")

if st.session_state['selected_movie'] is not None:
    # movie discription by movie id
    display_movie_details(st.session_state['selected_movie'])

    if st.button("Go Back"):
        st.session_state['selected_movie'] = None
        st.query_params.clear()
        time.sleep(1)
        st.rerun()


elif st.session_state['selected_genre'] is not None:
    # movie genre by movie id

    display_movie_of_genre(st.session_state['selected_genre'])
    # display_movie_of_genre("Action")
    if st.button("Go Back"):
        st.session_state['genre_type'] = None
        st.query_params.clear()
        time.sleep(1)
        st.rerun()



else:
    #
    # NAVBAR
    #


    #
    # MAIN CONTENT
    #



    # temphtml = f"""
    #             <a href="?genre_type=Action">
    #                 <h2>Action</h2>
    #             </a>
    #             """
    # st.markdown(temphtml, unsafe_allow_html=True)
    #
    # MOVIE SLIDER CAROUSEL
    #
    # st.write(get_specific_genre_movie("Action",10))
    st.markdown("<h2>Audience All-Stars✨</h2>", unsafe_allow_html=True)
    Movie_Slider()

    st.markdown("<h2>Get Movie Recommendation🔎</h2>", unsafe_allow_html=True)
    tab1, tab2 = st.tabs(["Get Recommendation By Movie", "Search By Filter"])
    # Movie Bases Recommendation
    with tab1:

        option = st.selectbox(
            "which movie is in your mind ?",
            movies_data["title"].values,
        )
        if st.button("SEARCH"):
            with st.spinner('Finding the perfect movies just for you...Sit tight!'):
                name, poster, mov_id = recommend_similar_movie(option)
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
                for i in (0, 5):
                    col1, col2, col3, col4, col5 = st.columns(5, gap="small", vertical_alignment="center")
                    with col1:
                        image_html = f"""
                                        <a href="?movie_id={mov_id[i]}">
                                            <img src="{poster[i]}" style="width: 13vw;" class="clickable-image"/>
                                        </a>
                                        """
                        st.markdown(image_html, unsafe_allow_html=True)
                        st.text(name[i])
                    with col2:
                        image_html = f"""
                                                    <a href="?movie_id={mov_id[i + 1]}">
                                                        <img src="{poster[i + 1]}" style="width: 13vw;" class="clickable-image"/>
                                                    </a>
                                                    """
                        st.markdown(image_html, unsafe_allow_html=True)
                        st.text(name[i + 1])
                    with col3:
                        image_html = f"""
                                                    <a href="?movie_id={mov_id[i + 2]}">
                                                        <img src="{poster[i + 2]}" style="width: 13vw;" class="clickable-image"/>
                                                    </a>
                                                    """
                        st.markdown(image_html, unsafe_allow_html=True)
                        st.text(name[i + 2])
                    with col4:
                        image_html = f"""
                                                    <a href="?movie_id={mov_id[i + 3]}">
                                                        <img src="{poster[i + 3]}" style="width: 13vw;" class="clickable-image"/>
                                                    </a>
                                                    """
                        st.markdown(image_html, unsafe_allow_html=True)
                        st.text(name[i + 3])
                    with col5:
                        image_html = f"""
                                                    <a href="?movie_id={mov_id[i + 4]}">
                                                        <img src="{poster[i + 4]}" style="width: 13vw;" class="clickable-image"/>
                                                    </a>
                                                    """
                        st.markdown(image_html, unsafe_allow_html=True)
                        st.text(name[i + 4])


    # Filter Bases Recommendation
    with tab2:
        unique_genres = ['Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
                         'Fantasy',
                         'Foreign', 'History', 'Horror', 'Music', 'Mystery', 'Romance', 'ScienceFiction', 'TVMovie',
                         'Thriller',
                         'War', 'Western']

        selected_genre = st.selectbox(
            "Select Genre",
            unique_genres
        )

        selected_year = st.slider(
            "Select Year",
            (movies_data["release_date"].min()).year,
            (movies_data["release_date"].max()).year,
            step=1
        )
        popularity_score = st.slider(
            "Select Popularity",
            int(movies_data["popularity"].min()),
            int(movies_data["popularity"].max()),
            step=1
        )
        if st.button("Recommend"):
            with st.spinner('Finding the perfect movies just for you...Sit tight!'):
                # st.write(selected_year,selected_genre,popularity_score)
                movies,extra = get_general_recommendations(genres=selected_genre, min_popularity=popularity_score, min_year=selected_year, top_n=15)
                total_recommend_movies = len(movies)
                total_extra_movies = len(extra)

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

                #
                # Extra Similar Recommendations
                #
                if movies == []:
                    # st.write("No eligible movies found.")
                    st.markdown("<h3 style='text-align: center; color: red;'>No eligible movies found.</h3>",
                                unsafe_allow_html=True)
                else:
                    st.markdown("<h3>Our Filtered Recommendation .</h3>",
                                unsafe_allow_html=True)

                for i in range(0, total_recommend_movies, 5):
                    # st.write("iter :",i)
                    col1, col2, col3, col4, col5 = st.columns(5, gap="medium", vertical_alignment="center")
                    if i < total_recommend_movies:
                        with col1:
                            image_html = f"""
                                                        <a href="?movie_id={movies[i][0]}">
                                                            <img src="{movies[i][2]}" style="width: 13vw;" class="clickable-image"/>
                                                        </a>
                                                        """
                            st.markdown(image_html, unsafe_allow_html=True)
                            st.text(movies[i][1])
                    if i+1 < total_recommend_movies:
                        with col2:
                            image_html = f"""
                                                                    <a href="?movie_id={movies[i+1][0]}">
                                                                        <img src="{movies[i+1][2]}" style="width: 13vw;" class="clickable-image"/>
                                                                    </a>
                                                                    """
                            st.markdown(image_html, unsafe_allow_html=True)
                            st.text(movies[i+1][1])
                    if i+2 < total_recommend_movies:
                        with col3:
                            image_html = f"""
                                                                    <a href="?movie_id={movies[i+2][0]}">
                                                                        <img src="{movies[i+2][2]}" style="width: 13vw;" class="clickable-image"/>
                                                                    </a>
                                                                    """
                            st.markdown(image_html, unsafe_allow_html=True)
                            st.text(movies[i+2][1])
                    if i+3 < total_recommend_movies:
                        with col4:
                            image_html = f"""
                                                                    <a href="?movie_id={movies[i+3][0]}">
                                                                        <img src="{movies[i+3][2]}" style="width: 13vw;" class="clickable-image"/>
                                                                    </a>
                                                                    """
                            st.markdown(image_html, unsafe_allow_html=True)
                            st.text(movies[i+3][1])
                    if i + 4 < total_recommend_movies:
                        with col5:
                            image_html = f"""
                                                                    <a href="?movie_id={movies[i+4][0]}">
                                                                        <img src="{movies[i+4][2]}" style="width: 13vw;" class="clickable-image"/>
                                                                    </a>
                                                                    """
                            st.markdown(image_html, unsafe_allow_html=True)
                            st.text(movies[i+4][1])
                #
                # Extra Similar Recommendations
                #
                st.markdown("<h3>Similar Movies You Would Like .</h3>",
                            unsafe_allow_html=True)
                for i in range(0, total_extra_movies, 5):
                    # st.write("iter :",i)
                    col1, col2, col3, col4, col5 = st.columns(5, gap="medium", vertical_alignment="center")
                    if i < total_extra_movies:
                        with col1:
                            image_html = f"""
                                                                    <a href="?movie_id={extra[i][0]}">
                                                                        <img src="{extra[i][2]}" style="width: 13vw;" class="clickable-image"/>
                                                                    </a>
                                                                    """
                            st.markdown(image_html, unsafe_allow_html=True)
                            st.text(extra[i][1])
                    if i + 1 < total_extra_movies:
                        with col2:
                            image_html = f"""
                                                                                <a href="?movie_id={extra[i + 1][0]}">
                                                                                    <img src="{extra[i + 1][2]}" style="width: 13vw;" class="clickable-image"/>
                                                                                </a>
                                                                                """
                            st.markdown(image_html, unsafe_allow_html=True)
                            st.text(extra[i + 1][1])
                    if i + 2 < total_extra_movies:
                        with col3:
                            image_html = f"""
                                                                                <a href="?movie_id={extra[i + 2][0]}">
                                                                                    <img src="{extra[i + 2][2]}" style="width: 13vw;" class="clickable-image"/>
                                                                                </a>
                                                                                """
                            st.markdown(image_html, unsafe_allow_html=True)
                            st.text(extra[i + 2][1])
                    if i + 3 < total_extra_movies:
                        with col4:
                            image_html = f"""
                                                                                <a href="?movie_id={extra[i + 3][0]}">
                                                                                    <img src="{extra[i + 3][2]}" style="width: 13vw;" class="clickable-image"/>
                                                                                </a>
                                                                                """
                            st.markdown(image_html, unsafe_allow_html=True)
                            st.text(extra[i + 3][1])
                    if i + 4 < total_extra_movies:
                        with col5:
                            image_html = f"""
                                                                                <a href="?movie_id={extra[i + 4][0]}">
                                                                                    <img src="{extra[i + 4][2]}" style="width: 13vw;" class="clickable-image"/>
                                                                                </a>
                                                                                """
                            st.markdown(image_html, unsafe_allow_html=True)
                            st.text(extra[i + 4][1])



