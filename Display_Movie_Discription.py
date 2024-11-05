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

from Recommendation_Model import similarity_matrix
from Recommendation_Model import movies_data


##############################################
######## MOVIE REVIEW SENTIMENT MODEL ########
##############################################
from Review_Sentiment_Analysis_Model import get_reviews
from Review_Sentiment_Analysis_Model import Review_sentiment




def display_movie_details(movie_id):
    ##############################################
    ######## MOVIE DISPLAY PART ##################
    ##############################################

    movie = movies_data[movies_data['movie_id'] == movie_id].iloc[0]
    st.image(get_poster_path(movie_id), width=230)
    st.header(movie['title'])
    st.write(get_discription(movie_id))
    st.write("Genres: ", ', '.join(movie['genres']))
    #
    # cast
    #
    st.subheader("CAST")
    cast_name, cast_character, cast_image = get_cast(movie_id)
    # Sample CSS for carousel
    carousel_style = """
    <style>
    .carousel {
        display: flex;
        overflow-x: auto;
        scroll-snap-type: x mandatory;
    }

    .card {
        flex: none;
        scroll-snap-align: center;
        margin-right: 20px;
        padding: 1.5%;
        background-color: #fff;
        border-radius: 10px;
        width: 30%;
    }

    .card img {
        width: 100%;
        height:100;
        border-radius: 2%;
    }

    .card-title {
        font-size: 1.2em;
        text-allign:center;
        color :black;
        margin: 1px;
    }


    </style>
    """

    # Sample HTML for carousel with cards
    start = '''
    <div class="carousel">
    '''
    # mid =

    end = '''    
    </div>
    <br>
    <br>
    '''
    for i in range(len(cast_name)):
        start += f"""
    <div class="card">
            <img src={cast_image[i]} alt="Card Image 2">
            <h3 class="card-title">{cast_name[i]} as {cast_character[i]}</h3>
        </div>

    """
    carousel_html = start + end
    # Insert CSS and HTML into Streamlit app
    st.markdown(carousel_style, unsafe_allow_html=True)
    st.markdown(carousel_html, unsafe_allow_html=True)

    #
    # REVIEWS
    #
    st.markdown(
        """
        <style>
        .scrollable-content {
            max-height: 300px;  /* Limit height */
            overflow-y: auto;   /* Enable vertical scroll if content overflows */
            padding: 10px;      /* Optional padding for better appearance */
            border: 1px solid #ddd;  /* Optional border for visual distinction */
            border-radius: 5px;  /* Rounded corners for aesthetics */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    samples_reviews = get_reviews(movie_id)
    # st.write(samples_reviews)
    tab1, tab2 = st.tabs(["Positive Reviews 😊", "Negative Reviews 😞"])
    positive_reviews, negative_reviews = Review_sentiment(samples_reviews)

    start_block = '<div class="scrollable-content">'
    end_block = "</div>"
    with tab1:

        start_block = '<div class="scrollable-content">'
        mid = ""
        if positive_reviews:
            for review in positive_reviews:
                mid += f"• {review[0]} <br>~{review[1]}<br><br>"

        else:
            mid += "No positive reviews yet."

        st.markdown(start_block + mid + end_block, unsafe_allow_html=True)

    with tab2:
        mid2 = ""
        if negative_reviews:
            for review in negative_reviews:
                mid2 += f"• {review[0]} <br>~{review[1]}<br><br>"
        else:
            mid2 += "No negative reviews yet."
        st.markdown(start_block + mid2 + end_block, unsafe_allow_html=True)

    #
    # OUR RECOMMENDATION
    #


    st.header("OUR RECOMMENDATIONS")
    with st.spinner('Finding the perfect movies just for you...Sit tight!'):
        disc_movie_name, disc_movie_poster, disc_movie_id = recommend_similar_movie(movie["title"])
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

        for i in (1, 5):
            col1, col2, col3, col4 = st.columns(4, gap="small", vertical_alignment="center")
            with col1:
                image_html = f"""
                            <a href="?movie_id={disc_movie_id[i]}">
                                <img src="{disc_movie_poster[i]}" style="width: 13vw;" class ="clickable-image"/>
                            </a>
                            """
                st.markdown(image_html, unsafe_allow_html=True)
                st.text(disc_movie_name[i])
            with col2:
                image_html = f"""
                            <a href="?movie_id={disc_movie_id[i + 1]}">
                                <img src="{disc_movie_poster[i + 1]}" style="width: 13vw;" class ="clickable-image"/>
                            </a>
                            """
                st.markdown(image_html, unsafe_allow_html=True)
                st.text(disc_movie_name[i + 1])
            with col3:
                image_html = f"""
                            <a href="?movie_id={disc_movie_id[i + 2]}">
                                <img src="{disc_movie_poster[i + 2]}" style="width: 13vw;" class ="clickable-image"/>
                            </a>
                            """
                st.markdown(image_html, unsafe_allow_html=True)
                st.text(disc_movie_name[i + 2])
            with col4:
                image_html = f"""
                            <a href="?movie_id={disc_movie_id[i + 3]}">
                                <img src="{disc_movie_poster[i + 3]}" style="width: 13vw;" class ="clickable-image"/>
                            </a>
                            """
                st.markdown(image_html, unsafe_allow_html=True)
                st.text(disc_movie_name[i + 3])
