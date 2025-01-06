import time

import streamlit as st
# import time
# from datetime import date
# from streamlit_navigation_bar import st_navbar

from streamlit_cookies_controller import CookieController


##############################################
######## MOVIE RECOMMENDATION MODEL ##########
##############################################
from Database_Management import add_user
# from Database_Management import remove_user
# from Database_Management import add_wishlist
# from Database_Management import get_wishlist
# from Database_Management import remove_wishlist


import firebase_admin
import pyrebase
import json

# from firebase_admin import credentials
# from firebase_admin import auth

if not firebase_admin._apps:
    # with open('flicknest-user-database-75b40c88a2c3.json') as f:
    #     cred = json.load(f)
    cred = {
   "apiKey": "AIzaSyBdHZguKt-XyUz32XeSYNMvNeOx0x-l3Tg",
   "databaseURL": "https://flicknest-user-database-default-rtdb.firebaseio.com/",
   "authDomain": "flicknest-user-database.firebaseapp.com",
   "projectId": "flicknest-user-database",
   "storageBucket": "flicknest-user-database.firebasestorage.app",
   "messagingSenderId": "496031991785",
   "appId": "1:496031991785:web:d1a07c9a159f6c606bad78",
   "measurementId": "G-YDQ0HSYS1G"
   }

    # cred = credentials.Certificate('flicknest-user-database-75b40c88a2c3.json')
    # firebase_admin.initialize_app(cred)
    firebase = pyrebase.initialize_app(cred)
    auth = firebase.auth()
    db = firebase.database()

def bg_image():
    background_image_css = """
    <style>
    [data-testid="stAppViewContainer"] > .main {{
        background: 
            linear-gradient(
                rgba(0, 0, 0, 0.4),  /* Semi-transparent overlay */
                rgba(0, 0, 0, 0.4)   /* Semi-transparent overlay */
            ), 
            url("https://maven-uploads.s3.amazonaws.com/120386748/projects/netflix%20image.jpg");         /* Background image */
        background-size: cover;        /* Ensure the image fills the container */
        background-position: center;   /* Center the image */
        background-repeat: no-repeat;  /* Prevent tiling */
    }}
    </style>
    """
    st.markdown(background_image_css, unsafe_allow_html=True)
# bg_image()


def app():
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
    bg_image()

    # st.title('Welcome to :orange[FlickNest]')
    st.markdown("<h1>Welcome to <span style='color:yellow;'>FlickNest</span></h1>", unsafe_allow_html=True)




    if "useremail" not in st.session_state:
        st.session_state.useremail = ""
    if "username" not in st.session_state:
        st.session_state.username = ""
    if "SignedIn" not in st.session_state:
        st.session_state.SignedIn = False
    if "SignOutPart" not in st.session_state:
        st.session_state.SignOutPart = False

    def Login(email, password):
        try:
            # user = auth.get_user_by_email(email)
            user = auth.sign_in_with_email_and_password(email=email, password=password)

            st.session_state.useremail = user["email"]
            st.session_state.username = user["localId"]
            st.session_state.SignedIn = True
            st.session_state.SignOutPart = True

            controller = CookieController()
            controller.set(name='FlickNest_useremail_cookie', value=st.session_state.useremail, max_age= 60*60*24)
            controller.set(name='FlickNest_password_cookie', value=password, max_age= 60*60*24)
            controller.set(name='FlickNest_userid_cookie', value=st.session_state.username, max_age= 60*60*24)


            st.success("Login Sucessfully!!")
            st.balloons()
            # time.sleep(5)
            # st.rerun()

        except:
            st.warning("Login Failed")
    def RemoveUser():
        st.session_state.SignedIn = False
        st.session_state.SignOutPart = False
        st.session_state.useremail = ""
        st.session_state.username = ""
        controller = CookieController()
        controller.remove(name='FlickNest_useremail_cookie')
        controller.remove(name='FlickNest_password_cookie')
        controller.remove(name='FlickNest_userid_cookie')

    controller = CookieController()
    Flicknest_email = controller.get(name='FlickNest_useremail_cookie')
    Flicknest_password = controller.get(name='FlickNest_password_cookie')
    Flicknest_userid = controller.get(name='FlickNest_userid_cookie')

    if Flicknest_email and Flicknest_password and Flicknest_userid:
        st.session_state["SignedIn"] = True
        st.session_state["SignOutPart"] = True
        st.session_state.username = Flicknest_userid
        st.session_state.useremail = Flicknest_email

    if st.session_state["SignedIn"] == False:
    
        choice = st.selectbox("Login/SignUp", ['Login', 'Sign Up'])

        if choice == "Login":
            # st.markdown("<h2>LOGIN</h2>", unsafe_allow_html=True)
            with st.form(key="login_form"):
                email = st.text_input("Enter Your Email Address")
                password = st.text_input("Password", type="password")
                login_button = st.form_submit_button(label="Login")

            if login_button:
                Login(email, password)

        else:

            # st.markdown("<h2>SignUp</h2>", unsafe_allow_html=True)
            with st.form(key="login_form"):
                User_email = st.text_input("Enter Your Email Address")
                User_password = st.text_input("Password", type="password")
                Signup_button = st.form_submit_button(label="Signup")

            # if st.button("Create Account"):
            if Signup_button:
                try:
                    user = auth.create_user_with_email_and_password(email = User_email,password = User_password)

                    add_user(user_id=user["localId"],user_email=User_email)
                    st.success("Account Created Succesfully ! Welcome To FlickNest Family :)")
                    st.markdown("Please Login With Your Email id And Password")
                    st.balloons()
                except:
                    st.warning("User Already Available")




    if st.session_state["SignOutPart"] == True:
        st.markdown(f"<h3>UserId : <span style='color:yellow;'>{st.session_state.username}</span></h3>", unsafe_allow_html=True)
        st.markdown(f"<h3>EmailId : <span style='color:yellow;'>{st.session_state.useremail}</span></h3>", unsafe_allow_html=True)
        st.button("SignOut",on_click = RemoveUser)






































