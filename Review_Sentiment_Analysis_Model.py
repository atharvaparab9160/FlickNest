import pickle
import requests
from datetime import date
import streamlit as st

##############################################
######## MOVIE REVIEW SENTIMENT MODEL ########
##############################################
model = pickle.load(open("model.pkl", "rb"))
scalar = pickle.load(open("scalar.pkl", "rb"))

def  get_reviews(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/reviews?language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3ZmVmNzU0YzcwNGE3N2QyMjI0NzFjNjBhNjdhZjcwMiIsIm5iZiI6MTczMDExNjg1NC41MTA1NzksInN1YiI6IjY0NGFiYjRhYjZhYmM0MDRlZDNhNmY2ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.viQ4SlUoftvEM5A90OAE1lHUbtshzjewstcayN1gUmY"
    }

    response = requests.get(url, headers=headers)

    data = response.json()
    if "results" not in data:
        return []
    reviews = data["results"]
    final_review = []
    for i in range(min(10,len(reviews))):
        name = reviews[i]["author"]
        time = reviews[i]["updated_at"]
        a = ""
        # print(name)
        # print(time)
        if time:
            time = reviews[i]["updated_at"][0:10]
            a = date(day=int(time[8:]), month=int(time[5:7]), year=int(time[0:4])).strftime('%A %d %B %Y')

        unk = "unknown"
        s = f"Review by {name if name else unk} On {a}"
        final_review.append([reviews[i]["content"],s])
    return final_review

def Review_sentiment(texts):
    pos = []
    neg = []
    for rev,time in texts:
        review_scalar = scalar.transform([rev]).toarray()
        result = model.predict(review_scalar)

        if result == 1:
            pos.append([rev,time])
        else:
            neg.append([rev,time])
    return pos,neg


