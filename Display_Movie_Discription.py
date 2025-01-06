import pandas as pd
import pickle
import requests
import streamlit as st
from datetime import date
from streamlit_navigation_bar import st_navbar

##############################################
######## DataBase Magament ##########
##############################################
from Database_Management import add_wishlist

from streamlit_cookies_controller import CookieController



##############################################
######## MOVIE RECOMMENDATION MODEL ##########
##############################################
from Recommendation_Model import get_cast
from Recommendation_Model import get_discription
from Recommendation_Model import get_poster_path
from Recommendation_Model import get_video_path
from Recommendation_Model import get_Movie_Banner
from Recommendation_Model import get_trending
from Recommendation_Model import recommend_similar_movie

from Recommendation_Model import similarity_matrix
from Recommendation_Model import movies_data


##############################################
######## MOVIE REVIEW SENTIMENT MODEL ########
##############################################
from Review_Sentiment_Analysis_Model import get_reviews
from Review_Sentiment_Analysis_Model import Review_sentiment


def bg_image(poster):
    background_image_css = f"""
    <style>
    [data-testid="stAppViewContainer"]{{
        background: 
            linear-gradient(
                rgba(0, 0, 0, 0.6),  /* Semi-transparent overlay */
                rgba(0, 0, 0, 0.6)   /* Semi-transparent overlay */
            ), 
            url("{poster}");         /* Background image */
        background-size: cover;        /* Ensure the image fills the container */
        background-position: center;   /* Center the image */
        background-repeat: no-repeat;  /* Prevent tiling */
    }}
    [data-testid="stHeader"]{{
            background: 
                linear-gradient(
                    rgba(0, 0, 0, 0.6),  /* Semi-transparent overlay */
                    rgba(0, 0, 0, 0.6)   /* Semi-transparent overlay */
                ), 
                url("https://maven-uploads.s3.amazonaws.com/120386748/projects/netflix%20image.jpg"); /* Background image */
            background-size: cover;        /* Adjust to fill the container */
            background-position: center;   /* Center the image */
            background-repeat: no-repeat;  /* Prevent tiling */
        }}
    </style>
    """
    st.markdown(background_image_css, unsafe_allow_html=True)

def display_movie_details(movie_id):
    ##############################################
    ######## MOVIE DISPLAY PART ##################
    ##############################################
    poster = get_Movie_Banner(movie_id)
    bg_image(poster)


    movie = movies_data[movies_data['movie_id'] == movie_id].iloc[0]
    # st.write(movies_data[movies_data['movie_id'] == movie_id].iloc[0])
    movie_vdo_path = get_video_path(movie_id)
    col1, col2 = st.columns([1,2.60])
    with col1:
        st.image(get_poster_path(movie_id), width=230)
    with col2:
        # fff = "https://youtu.be/dEfzQkfb60E?si=SlAbaqCTLjBStX3f"
        st.video(movie_vdo_path, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False,
                 muted=False)

    st.header(movie['title'])
    st.write(get_discription(movie_id))
    # st.write("GENRES: ", ', '.join(movie['genres']))
    st.markdown(f"<h5>Genres : {', '.join(movie['genres'])}</h5>",
                unsafe_allow_html=True)


    #
    # wishlist
    #
    # def add_to_wishlist(movie_id):
    #     st.success(f"Movie with ID {movie_id} has been added to the wishlist!")


    # Add global CSS styling for the button appearance
    st.markdown("""
        <style>
        .st-key-image_button button {
            background: url('https://i.ibb.co/gwQpsfx/wishlist.png') no-repeat center;
            background-size: cover;
            width: 50px;
            height: 50px;
            border: none;
            cursor: pointer;
            text-indent: -9999px;
        }
        </style>
    """, unsafe_allow_html=True)


    # https://i.ibb.co/gwQpsfx/heart.png  filled
    # https://i.ibb.co/CVygC1g/wishlist.png    empty
    controller = CookieController()
    user_id = controller.get(name='FlickNest_userid_cookie')
    # print(user_id)

    # Create a button that triggers the function
    if st.button("Add to Wishlist", key="image_button"):
        # add_to_wishlist(movie_id)
        controller = CookieController()
        user_id = controller.get(name='FlickNest_userid_cookie')
        # print(Flicknest_userid,Flicknest_password,Flicknest_email)
        if user_id!=None:
            add_wishlist(user_id,movie_id,movie['title'])
        else:
            st.warning("Login To Create a Wishlist!!")


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
        text-align:center;
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
            <span class="card-title">{cast_name[i]} as {cast_character[i]}</span>
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
                # st.text(disc_movie_name[i])
                st.markdown(
                    f"""
                                                                                    <div style="overflow-x: auto; white-space: nowrap;">
                                                                                        {disc_movie_name[i]}
                                                                                    </div>
                                                                                    """,
                    unsafe_allow_html=True
                )
            with col2:

                image_html = f"""
                            <a href="?movie_id={disc_movie_id[i + 1]}">
                                <img src="{disc_movie_poster[i + 1]}" style="width: 13vw;" class ="clickable-image"/>
                            </a>
                            """
                st.markdown(image_html, unsafe_allow_html=True)
                # st.text(disc_movie_name[i + 1])
                st.markdown(
                    f"""
                                                                    <div style="overflow-x: auto; white-space: nowrap;">
                                                                        {disc_movie_name[i + 1]}
                                                                    </div>
                                                                    """,
                    unsafe_allow_html=True
                )
            with col3:
                image_html = f"""
                            <a href="?movie_id={disc_movie_id[i + 2]}">
                                <img src="{disc_movie_poster[i + 2]}" style="width: 13vw;" class ="clickable-image"/>
                            </a>
                            """
                st.markdown(image_html, unsafe_allow_html=True)
                # st.text(disc_movie_name[i + 2])
                st.markdown(
                    f"""
                                                                    <div style="overflow-x: auto; white-space: nowrap;">
                                                                        {disc_movie_name[i + 2]}
                                                                    </div>
                                                                    """,
                    unsafe_allow_html=True
                )
            with col4:
                image_html = f"""
                            <a href="?movie_id={disc_movie_id[i + 3]}">
                                <img src="{disc_movie_poster[i + 3]}" style="width: 13vw;" class ="clickable-image"/>
                            </a>
                            """
                st.markdown(image_html, unsafe_allow_html=True)
                # st.text(disc_movie_name[i + 3])
                st.markdown(
                    f"""
                                                    <div style="overflow-x: auto; white-space: nowrap;">
                                                        {disc_movie_name[i + 3]}
                                                    </div>
                                                    """,
                    unsafe_allow_html=True
                )
