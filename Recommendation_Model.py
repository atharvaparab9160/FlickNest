import pandas as pd
import requests
import streamlit as st
import pickle
##############################################
######## MOVIE RECOMMENDATION MATRIX #########
##############################################

movie_sample_bin = pickle.load(open("movies_data.pkl", "rb"))
similarity_matrix = pickle.load(open("similarity_matrix.pkl", "rb"))
movies_data = pd.DataFrame(movie_sample_bin)

def get_movie_data(m_id):
    url = f"https://api.themoviedb.org/3/movie/{m_id}?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3ZmVmNzU0YzcwNGE3N2QyMjI0NzFjNjBhNjdhZjcwMiIsIm5iZiI6MTcyNTk5NzEwNi40ODM0MjgsInN1YiI6IjY0NGFiYjRhYjZhYmM0MDRlZDNhNmY2ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.UKJFace1HPCyEG3AuLp22sAREDx9T5ePz48fi-uiRdw"
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    return data

def get_movie_data_from_list(m_list):
    all_movie_data = []
    for m_id in m_list:
        url = f"https://api.themoviedb.org/3/movie/{m_id}?language=en-US"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3ZmVmNzU0YzcwNGE3N2QyMjI0NzFjNjBhNjdhZjcwMiIsIm5iZiI6MTcyNTk5NzEwNi40ODM0MjgsInN1YiI6IjY0NGFiYjRhYjZhYmM0MDRlZDNhNmY2ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.UKJFace1HPCyEG3AuLp22sAREDx9T5ePz48fi-uiRdw"
        }

        response = requests.get(url, headers=headers)
        data = response.json()

        base = "https://image.tmdb.org/t/p/w500/"
        # base = "https://image.tmdb.org/t/p/original"
        if "poster_path" not in data:
            base += "ij9800Kzdff5u9Ki6FT3eex0Ap7.jpg"
        if data["poster_path"] != None:
            base += data["poster_path"]
        else:
            base += "ij9800Kzdff5u9Ki6FT3eex0Ap7.jpg"

        name = data["title"]
        poster = base
        m_data = [m_id,name,poster]
        all_movie_data.append(m_data)
    return all_movie_data
def get_poster_path(m_id):

    data = get_movie_data(m_id)
    # print(data)
    # st.write(data)

    base = "https://image.tmdb.org/t/p/w500/"
    # base = "https://image.tmdb.org/t/p/original"
    if "poster_path" not in data:
        return base + "ij9800Kzdff5u9Ki6FT3eex0Ap7.jpg"
    if data["poster_path"] != None:
        return base + data["poster_path"]
    else:
        return base + "ij9800Kzdff5u9Ki6FT3eex0Ap7.jpg"

def get_video_path(m_id):
    url = f"https://api.themoviedb.org/3/movie/{m_id}/videos?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3ZmVmNzU0YzcwNGE3N2QyMjI0NzFjNjBhNjdhZjcwMiIsIm5iZiI6MTY4MjYxOTIxMC42NTI5OTk5LCJzdWIiOiI2NDRhYmI0YWI2YWJjNDA0ZWQzYTZmNmQiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.T4EZvbPBHcagISBmcwA1plqdNm5xKriGOyEM2uC1qg8"
    }

    response = requests.get(url, headers=headers)

    data = response.json()
    # st.write(data)
    base = "https://www.youtube.com/watch?v="
    # st.write(data["results"][-1]["site"])
    try:
        if data["results"][-1]["site"] == "YouTube":
            v_link = data["results"][-1]["key"]
            return base + v_link
        else:
            return base + "dEfzQkfb60E"



    except:
        return base + "dEfzQkfb60E"



def get_Movie_Banner(m_id):

    data = get_movie_data(m_id)
    # st.write(data)

    base = "https://image.tmdb.org/t/p/original"
    if data["backdrop_path"] != None:
        return base + data["backdrop_path"]
    else:
        return base + "/fhv3dWOuzeW9eXOSlr8MCHwo24t.jpg"



def get_discription(m_id):
    data = get_movie_data(m_id)
    # print(data)
    if "overview" not in data:
        return "Discription Not Available"
    if data["overview"] != None:

        return data["overview"]
    else:
        return "Discription Not Available"


def get_cast(m_id):

    url = f"https://api.themoviedb.org/3/movie/{m_id}/credits?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3ZmVmNzU0YzcwNGE3N2QyMjI0NzFjNjBhNjdhZjcwMiIsIm5iZiI6MTcyNjEzNDY3Ny41OTQwMTEsInN1YiI6IjY0NGFiYjRhYjZhYmM0MDRlZDNhNmY2ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mlbHDN6JQtS7Zzq1FidSNy2rQRHpCYHVKULdmH9UT-8"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    if "cast" not in data:
        st.write("CAST NOT FOUND")
        return [],[],[]

    name = []
    character = []
    image = []
    base = "https://image.tmdb.org/t/p/w200/"
    for i in range(min(len(data["cast"]), 8)):
        name.append(data["cast"][i]["name"])
        character.append(data["cast"][i]["character"])
        if data["cast"][i]["name"] != None and data["cast"][i]["profile_path"] != None:
            image.append(base + data["cast"][i]["profile_path"])
        else:
            image.append(base + "ij9800Kzdff5u9Ki6FT3eex0Ap7.jpg")

    # st.write(name, character, image)
    if name == [] and character == [] and image == []:
        st.write("CAST NOT FOUND")
        return [],[],[]
    return name, character, image


def get_trending(count):
    movies_list = []
    top_movies = movies_data.sort_values(by="popularity", ascending=False).head(count)
    x = top_movies["movie_id"]

    for m_id in x:
        data = get_movie_data(m_id)
        temp = []
        base = "https://image.tmdb.org/t/p/original"
        # title
        temp.append(data["title"])

        # genres
        gen = ""
        for i in data["genres"]:
            gen+=f'{i["name"]}, '
        temp.append(gen[:-2])

        # image
        if data["backdrop_path"] != None:
            temp.append(base + data["backdrop_path"])
        else:
            temp.append(base + "/fhv3dWOuzeW9eXOSlr8MCHwo24t.jpg")

        # overview
        temp.append(data["overview"])

        # rating
        temp.append(data["vote_average"])
        #movie_id
        temp.append(m_id)
        movies_list.append(temp)
    return movies_list



    # print(top_movies)

def recommend_similar_movie(input_movie):
    movie_index = movies_data[movies_data["title"] == input_movie].index[0]
    list_id = []
    list_movie = []
    list_poster = []
    distances = similarity_matrix[movie_index]
    similar_movie = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:10]

    for m in similar_movie:
        # print(m) == (sr_no,similarity)
        id = movies_data.iloc[m[0]].movie_id
        list_id.append(id)
        list_poster.append(get_poster_path(id))
        list_movie.append(movies_data.iloc[m[0]].title)

    # print(list_movie,list_poster)
    return list_movie, list_poster, list_id


def get_general_recommendations(genres=None, min_popularity=None, min_year=None, top_n=8):
    # Filter movies based on genres, popularity, and release year
    # print(movies_data.iterrows())
    # for i in movies_data.iterrows():
    #     st.write(i[0],i[1])
    #     st.write(i[0],i[1]["movie_id"])
    #     break
    eligible_indices = []
    null_recommendation = False

    for i, movie in movies_data.iterrows():
        if ((genres is None or  genres in movie['genres']) and
            (min_popularity is None or int(movie['popularity']) >= min_popularity) and
            (min_year is None or movie['release_date'].year >= min_year)):
            eligible_indices.append(i)

            # (min_year is None or pd.to_datetime(movie['release_date']).year >= min_year))


    # If no movies are eligible, return an empty list
    if not eligible_indices:
        null_recommendation = True
        # st.write("empty")
        for i, movie in movies_data.iterrows():
            if ((genres is None or genres in movie['genres'])):
                eligible_indices.append(i)
            if len(eligible_indices) >= top_n:
                break

    # Calculate the mean similarity vector only for eligible movies
    eligible_sim_matrix = similarity_matrix[eligible_indices, :]
    mean_similarity = eligible_sim_matrix.mean(axis=0)
    # st.write(mean_similarity)

    # Sort movies by their average similarity score
    sorted_indices = mean_similarity.argsort()[::-1]

    # Collect top_n recommended movies based on similarity scores
    recommendations = []
    extra = []
    for idx in sorted_indices:
        # Ensure we are recommending from the original movies DataFrame
        if idx in eligible_indices:
            if len(recommendations) >= top_n:
                continue
            movie = movies_data.iloc[idx]
            m_id = int(movie["movie_id"])
            recommendations.append([m_id, movie['title'],get_poster_path(m_id)])
        else:
            if len(extra) >= top_n:
                continue
            else:
                movie = movies_data.iloc[idx]
                m_id = int(movie["movie_id"])
                extra.append([m_id, movie['title'],get_poster_path(m_id)])

        if len(recommendations) >= top_n and len(extra) >= top_n :
            break
    # print(recommendations)
    if null_recommendation:
        return [],extra
    return recommendations, extra

def get_movies_recommendation_using_wishlist(movies_mid):

    eligible_indices = []

    for i, movie in movies_data.iterrows():
        if (str(movie["movie_id"]) in movies_mid):
            eligible_indices.append(i)
    # st.write(eligible_indices)

    # Calculate the mean similarity vector only for eligible movies
    eligible_sim_matrix = similarity_matrix[eligible_indices, :]
    # st.write(eligible_sim_matrix)
    mean_similarity = eligible_sim_matrix.mean(axis=0)
    # st.write(mean_similarity)

    # Sort movies by their average similarity score
    sorted_indices = mean_similarity.argsort()[::-1]
    # st.write(sorted_indices)

    movies_list = []
    cnt = 0
    for idx in sorted_indices:
        movie = movies_data.iloc[idx]
        m_id = str(movie["movie_id"])

        if m_id not in movies_mid:
            movies_list.append([int(m_id), movie['title'], get_poster_path(int(m_id))])
            cnt+=1
        if cnt == 20:
            break


    return movies_list




def get_specific_genre_movie(genre,no_of_movies):
    genre_movies = movies_data[movies_data['genres'].apply(lambda x: genre in x)]

    genre_movies = genre_movies.sort_values(by="popularity",ascending=False).head(no_of_movies)


    # st.write(genre_movies.head())
    return_movie_list = []
    for i,movie in genre_movies.iterrows():
        m_id = int(movie["movie_id"])
        return_movie_list.append([m_id,movie["title"],get_poster_path(m_id)])

    return return_movie_list




