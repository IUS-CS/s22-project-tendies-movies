import random
from imdb import Cinemagoer

class MovieClass:
    #Basic constructor for movie elements
    def __init__(self):
        self.movies = []
        self.index = 0
        self.cinemagoer = Cinemagoer()
        self.movie_obj = None

    # Get top 250 movies
    def import_top250(self):
        self.movies = self.cinemagoer.get_top250_movies()
        self.movie_obj = None
        self.index = 0

    # Takes a list of genres and removes all movies that are not
    # any of those genres
    def select_genre(self, genres):
        self.movies = self.cinemagoer.get_top50_movies_by_genres(genres)
        self.movie_obj = None
        self.index = 0
        
    # Append a movie to the movie list
    def append(self, movie):
        self.movies.append(movie)

    # Increment to the next movie in the list
    def next(self):
        #Set movie_obj to null
        self.movie_obj = None

        #if we don't go out of bounds, increment
        if self.index < len(self.movies):
            self.index += 1
        else:
            raise Exception("Movie list is out of bounds.")
        #otherwise, just stay at the end of the list

    # Return the movie object of the current movie
    def movie_object(self):
        #If there is not a movie object for the current film, make one
        if self.movie_obj == None:
            id = self.movies[self.index].getID()
            self.movie_obj = self.cinemagoer.get_movie(id)
        return self.movie_obj

    # Randomize the internal movie list
    def randomize(self):
        random.shuffle(self.movies)
        self.movie_obj = None
        self.index = 0

    # Return the title of the current movie
    def title(self):
        return self.movies[self.index]["title"]

    # Return the current movie rating
    def rating(self):
        try:
            return self.movie_object()["rating"]
        except:
            return "No Rating"

    # Return the URL for the cover image of the current movie
    def cover_url(self):
        return self.movie_object()["full-size cover url"]

    def plot_summary(self):
        return self.movie_object()["plot summary"]

    def genres(self):
        #We don't actually need to go create a movie object
        #for the genres, since we included it in the default information
        #set on line 6
        return self.movie_object()["genres"] 