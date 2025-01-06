import streamlit as st
from streamlit_cookies_controller import CookieController


##############################################
######## MOVIE RECOMMENDATION MODEL ##########
##############################################
from Database_Management import add_user
from Database_Management import remove_user
from Database_Management import add_wishlist
from Database_Management import get_wishlist
from Database_Management import remove_wishlist

##############################################
######## MOVIE RECOMMENDATION MODEL ##########
##############################################
from Recommendation_Model import get_movie_data_from_list , get_movies_recommendation_using_wishlist

import pyrebase
import mysql.connector



def bg_image():
    background_image_css = """
        <style>
        [data-testid="stAppViewContainer"]{
            background: 
                linear-gradient(rgba(0,0,0, 0.6), rgba(0,0,0, 0.6)), /* Semi-transparent overlay */
                url("https://maven-uploads.s3.amazonaws.com/120386748/projects/netflix%20image.jpg"); /* Background image */
            background-size: cover; /* Adjust to fill the container */
            background-position: center;  
            background-repeat: no-repeat;
        }
        [data-testid="stHeader"] {
            background: 
                linear-gradient(
                    rgba(0, 0, 0, 0.6),  /* Semi-transparent overlay */
                    rgba(0, 0, 0, 0.6)   /* Semi-transparent overlay */
                ), 
                url("https://maven-uploads.s3.amazonaws.com/120386748/projects/netflix%20image.jpg"); /* Background image */
            background-size: cover;        /* Adjust to fill the container */
            background-position: center;   /* Center the image */
            background-repeat: no-repeat;  /* Prevent tiling */
        }
        </style>
        """
    # Apply the CSS
    st.markdown(background_image_css, unsafe_allow_html=True)

def app():
    bg_image()


    # st.header("Specially For U")
    controller = CookieController()
    Flicknest_email = controller.get(name='FlickNest_useremail_cookie')
    Flicknest_password = controller.get(name='FlickNest_password_cookie')
    Flicknest_userid = controller.get(name='FlickNest_userid_cookie')
    # print(Flicknest_userid, Flicknest_password, Flicknest_email)

    if Flicknest_email and Flicknest_password and Flicknest_userid:
        st.header("WELCOME VIP USER💝!!!")


        movies_wishlist = []
        if get_wishlist(Flicknest_userid) != None:
            movies_wishlist = get_wishlist(Flicknest_userid)


        # st.write(movies_wishlist)
        movies = get_movie_data_from_list(movies_wishlist)
        total_wishlist_movies = len(movies_wishlist)
        st.markdown("<h1>Your Wishlist ❤️.</h1>",
                    unsafe_allow_html=True)
        if movies == []:
            # st.write("No eligible movies found.")
            st.markdown("<h3 style='text-align: center; color: red;'>Wishlist Is Empty.</h3>",
                        unsafe_allow_html=True)
        else:
            for i in range(0, total_wishlist_movies, 5):
                # st.write("iter :",i)
                col1, col2, col3, col4, col5 = st.columns(5, gap="medium", vertical_alignment="center")
                if i < total_wishlist_movies:
                    with col1:
                        image_html = f"""
                                                    <a href="?movie_id={movies[i][0]}">
                                                        <img src="{movies[i][2]}" style="width: 13vw;" class="clickable-image"/>
                                                    </a>
                                                    """
                        st.markdown(image_html, unsafe_allow_html=True)
                        # st.text(movies[i][1])
                        st.markdown(
                            f"""
                                <div style="overflow-x: auto; white-space: nowrap;">
                                    {movies[i][1]}
                                </div>
                            """,
                            unsafe_allow_html=True
                        )
                        if st.button("Remove",key=f"r{i}"):
                            remove_wishlist(Flicknest_userid,movies[i][0],movies[i][1])
                if i + 1 < total_wishlist_movies:
                    with col2:
                        image_html = f"""
                                                                <a href="?movie_id={movies[i + 1][0]}">
                                                                    <img src="{movies[i + 1][2]}" style="width: 13vw;" class="clickable-image"/>
                                                                </a>
                                                                """
                        st.markdown(image_html, unsafe_allow_html=True)
                        # st.text(movies[i + 1][1])
                        st.markdown(
                            f"""
                                <div style="overflow-x: auto; white-space: nowrap;">
                                    {movies[i + 1][1]}
                                </div>
                            """,
                            unsafe_allow_html=True
                        )
                        if st.button("Remove",key=f"r{i+1}"):
                            remove_wishlist(Flicknest_userid,movies[i+1][0],movies[i + 1][1])
                if i + 2 < total_wishlist_movies:
                    with col3:
                        image_html = f"""
                                                                <a href="?movie_id={movies[i + 2][0]}">
                                                                    <img src="{movies[i + 2][2]}" style="width: 13vw;" class="clickable-image"/>
                                                                </a>
                                                                """
                        st.markdown(image_html, unsafe_allow_html=True)
                        # st.text(movies[i + 2][1])
                        st.markdown(
                            f"""
                                <div style="overflow-x: auto; white-space: nowrap;">
                                    {movies[i + 2][1]}
                                </div>
                            """,
                            unsafe_allow_html=True
                        )
                        if st.button("Remove",key=f"r{i+2}"):
                            remove_wishlist(Flicknest_userid,movies[i+2][0],movies[i + 2][1])
                if i + 3 < total_wishlist_movies:
                    with col4:
                        image_html = f"""
                                                                <a href="?movie_id={movies[i + 3][0]}">
                                                                    <img src="{movies[i + 3][2]}" style="width: 13vw;" class="clickable-image"/>
                                                                </a>
                                                                """
                        st.markdown(image_html, unsafe_allow_html=True)
                        # st.text(movies[i + 3][1])
                        st.markdown(
                            f"""
                                <div style="overflow-x: auto; white-space: nowrap;">
                                    {movies[i + 3][1]}
                                </div>
                            """,
                            unsafe_allow_html=True
                        )
                        if st.button("Remove",key=f"r{i+3}"):
                            remove_wishlist(Flicknest_userid,movies[i+3][0],movies[i + 3][1])
                if i + 4 < total_wishlist_movies:
                    with col5:
                        image_html = f"""
                                                                <a href="?movie_id={movies[i + 4][0]}">
                                                                    <img src="{movies[i + 4][2]}" style="width: 13vw;" class="clickable-image"/>
                                                                </a>
                                                                """
                        st.markdown(image_html, unsafe_allow_html=True)
                        # st.text(movies[i + 4][1])
                        st.markdown(
                            f"""
                                <div style="overflow-x: auto; white-space: nowrap;">
                                    {movies[i + 4][1]}
                                </div>
                            """,
                            unsafe_allow_html=True
                        )
                        if st.button("Remove",key=f"r{i+4}"):
                            remove_wishlist(Flicknest_userid,movies[i+4][0],movies[i + 4][1])



        st.markdown("<h1>Specials As Per Your Taste ❤️.</h1>",
                    unsafe_allow_html=True)


        if movies_wishlist == []:
            st.markdown("<h3 style='text-align: center; color: red;'>Wishlist Is Empty.</h3>",
                    unsafe_allow_html=True)
        else:
            Recommended_movies_wishlist = get_movies_recommendation_using_wishlist(movies_wishlist)
            # st.write(Recommended_movies_wishlist)
            Total_Recommended_movies_wishlist = len(Recommended_movies_wishlist)
            for i in range(0, Total_Recommended_movies_wishlist, 5):
                # st.write("iter :",i)
                col1, col2, col3, col4, col5 = st.columns(5, gap="medium", vertical_alignment="center")
                if i < Total_Recommended_movies_wishlist:
                    with col1:
                        image_html = f"""
                                                    <a href="?movie_id={Recommended_movies_wishlist[i][0]}">
                                                        <img src="{Recommended_movies_wishlist[i][2]}" style="width: 13vw;" class="clickable-image"/>
                                                    </a>
                                                    """
                        st.markdown(image_html, unsafe_allow_html=True)
                        # st.text(Recommended_movies_wishlist[i][1])
                        st.markdown(
                            f"""
                                                            <div style="overflow-x: auto; white-space: nowrap;">
                                                                {Recommended_movies_wishlist[i][1]}
                                                            </div>
                                                        """,
                            unsafe_allow_html=True
                        )
                if i + 1 < Total_Recommended_movies_wishlist:
                    with col2:
                        image_html = f"""
                                                                <a href="?movie_id={Recommended_movies_wishlist[i + 1][0]}">
                                                                    <img src="{Recommended_movies_wishlist[i + 1][2]}" style="width: 13vw;" class="clickable-image"/>
                                                                </a>
                                                                """
                        st.markdown(image_html, unsafe_allow_html=True)
                        # st.text(Recommended_movies_wishlist[i + 1][1])
                        st.markdown(
                            f"""
                                                            <div style="overflow-x: auto; white-space: nowrap;">
                                                                {Recommended_movies_wishlist[i + 1][1]}
                                                            </div>
                                                        """,
                            unsafe_allow_html=True
                        )
                if i + 2 < Total_Recommended_movies_wishlist:
                    with col3:
                        image_html = f"""
                                                                <a href="?movie_id={Recommended_movies_wishlist[i + 2][0]}">
                                                                    <img src="{Recommended_movies_wishlist[i + 2][2]}" style="width: 13vw;" class="clickable-image"/>
                                                                </a>
                                                                """
                        st.markdown(image_html, unsafe_allow_html=True)
                        # st.text(Recommended_movies_wishlist[i + 2][1])
                        st.markdown(
                            f"""
                                                            <div style="overflow-x: auto; white-space: nowrap;">
                                                                {Recommended_movies_wishlist[i + 2][1]}
                                                            </div>
                                                        """,
                            unsafe_allow_html=True
                        )
                if i + 3 < Total_Recommended_movies_wishlist:
                    with col4:
                        image_html = f"""
                                                                <a href="?movie_id={Recommended_movies_wishlist[i + 3][0]}">
                                                                    <img src="{Recommended_movies_wishlist[i + 3][2]}" style="width: 13vw;" class="clickable-image"/>
                                                                </a>
                                                                """
                        st.markdown(image_html, unsafe_allow_html=True)
                        # st.text(Recommended_movies_wishlist[i + 3][1])
                        st.markdown(
                            f"""
                                                            <div style="overflow-x: auto; white-space: nowrap;">
                                                                {Recommended_movies_wishlist[i + 3][1]}
                                                            </div>
                                                        """,
                            unsafe_allow_html=True
                        )
                if i + 4 < Total_Recommended_movies_wishlist:
                    with col5:
                        image_html = f"""
                                                                <a href="?movie_id={Recommended_movies_wishlist[i + 4][0]}">
                                                                    <img src="{Recommended_movies_wishlist[i + 4][2]}" style="width: 13vw;" class="clickable-image"/>
                                                                </a>
                                                                """
                        st.markdown(image_html, unsafe_allow_html=True)
                        # st.text(Recommended_movies_wishlist[i + 4][1])
                        st.markdown(
                            f"""
                                                            <div style="overflow-x: auto; white-space: nowrap;">
                                                                {Recommended_movies_wishlist[i + 4][1]}
                                                            </div>
                                                        """,
                            unsafe_allow_html=True
                        )















    else:
        st.header("Signup To Access This Feature ")
