import webbrowser
import urllib
import json


def info(movie):
    # Getting details of requested Movie URL
    response = urllib.urlopen("http://www.omdbapi.com/?t=" +
                              movie + "&y=&plot=short&r=json")
    # Reading Data recieved in form of JSON
    output = response.read()
    # Extracting the Value from Output variable
    wjdata = json.loads(output)
    return wjdata


class Movie():
    """
        This class provides a way to solve to store
        movie related information
        title : indicates title of movie
        rating : indicates dynamic rating shown for movie
        trailer_youtube_url : indicates link of respective movie trailer url
        poster_image_url : indicates link of respective movie poster url
        storyline : brief decription of movie """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    # Constructor For Movie Class

    def __init__(self, movie_title, trailer_youtube):
        data = info(movie_title)
        self.rating = data['imdbRating']
        self.title = data['Title']
        self.storyline = data['Plot']
        self.poster_image_url = data['Poster']
        self.trailer_youtube_url = trailer_youtube
    # Open the Youtube trailer of Specified Movie

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
