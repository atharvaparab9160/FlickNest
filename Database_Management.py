import time

import pyrebase
import streamlit as st

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

def add_wishlist(user_id,m_id,m_name = "Movie"):
    # print("okkkkkkk",user_id,m_id)
    firebase = pyrebase.initialize_app(cred)
    db = firebase.database()

    list = db.child("users").child(user_id).child("wishlist").get().val()
    if list == None:
        list = []
    if str(m_id) not in list:
        list.append(str(m_id))
        db.child("users").child(user_id).update({"wishlist": list})
        st.success(f"{m_name} Added in Wishlist")
        st.toast(f"{m_name} Added in Wishlist",icon="🎉")
    else:
        st.warning("Movie already in wishlist")



def add_user(user_id,user_email):
    firebase = pyrebase.initialize_app(cred)
    db = firebase.database()
    data = {
        "user_email": user_email,
        "wishlist": ["211672"]
    }
    db.child("users").child(user_id).set(data)


def remove_user(user_id):
    firebase = pyrebase.initialize_app(cred)
    db = firebase.database()
    db.child("users").child(user_id).remove()

def remove_wishlist(user_id,m_id,m_name = "Movie"):
    firebase = pyrebase.initialize_app(cred)
    db = firebase.database()
    list = db.child("users").child(user_id).child("wishlist").get().val()
    if str(m_id) in list:
        list.remove(str(m_id))
        db.child("users").child(user_id).update({"wishlist": list})
        # st.success("Movie removed from Wishlist")
        st.toast(f"{m_name} Removed From Wishlist",icon = "🚨")
        time.sleep(1)
        st.rerun()
    else:
        # st.warning("Movie Not in wishlist , Can't Remove Movie")
        st.toast(f"Movie Not in wishlist , Can't Remove Movie", icon="🚨")

def get_wishlist(user_id):
    firebase = pyrebase.initialize_app(cred)
    db = firebase.database()
    list = db.child("users").child(user_id).child("wishlist").get().val()
    return list


