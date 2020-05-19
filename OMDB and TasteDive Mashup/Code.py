
import requests_with_caching
import json
def get_movie_data(movieName):
    para = {}
    para['t'] = movieName
    para['r'] = "json"
    url = 'http://www.omdbapi.com/'
    response = requests_with_caching.get(url, params = para)
    res = response.json()
    print(response.url)
    return(res)

def get_movie_rating(movieData):
    s=""
    for rating in movieData["Ratings"]:
        if rating["Source"]== "Rotten Tomatoes":
            s = rating["Value"]
    if s != "":
        r = int(s[:2])
    else: r = 0
    return r
def get_movies_from_tastedive(movie):
    para = {}
    para['q'] = movie
    para['type'] = "movies"
    para['limit'] = 5
    url = 'https://tastedive.com/api/similar'
    
    response = requests_with_caching.get(url, params = para)
    res = response.json()
    print(response.url)
    return(res)
def extract_movie_titles(data):
    result=[]
    for movie in data['Similar']['Results']:
        result.append(movie['Name'])
    return result
def get_related_titles(movieTitles):
    result=[]
    for movie in movieTitles:
        data=get_movies_from_tastedive(movie)
        names=extract_movie_titles(data)
        for name in names:
            if name not in result:
                result.append(name)
    return result
def get_sorted_recommendations(movieTitles):
    result=get_related_titles(movieTitles)
    result=sorted(result, key=lambda movieName:(get_movie_rating(get_movie_data(movieName)),movieName), reverse=True)
    return result
get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])




