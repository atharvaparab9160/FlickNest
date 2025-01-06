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
<<<<<<< Updated upstream
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
            int(100),
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



=======
>>>>>>> Stashed changes
