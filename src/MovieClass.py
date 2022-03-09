import random
from imdb import Cinemagoer

class MovieClass:
    #Basic constructor for movie elements
    def __init__(self):
        self.movies = []
        self.index = 0
        self.cinemagoer = Cinemagoer()
        self.movie_obj = 0

    # Get top 250 movies
    def import_top250(self):
        self.movies = self.cinemagoer.get_top250_movies()
        
        # Update the movie object variable
        self.movie_object()

    # Import a list of movies into the class
    def add(self, movie_list):
        self.movies = movie_list
        self.index = 0
        self.movie_object()

    # Append a movie to the movie list
    def append(self, movie):
        self.movies.append(movie)
    
    # Increment to the next movie in the list
    def next(self):
        #if we don't go out of bounds, increment
        if self.index < len(self.movies):
            self.index += 1
        else:
        #otherwise, wrap around to 0
            self.index = 0
        
        # Update the movie object variable
        self.movie_object()

    # Return the movie object of the current movie
    def movie_object(self):
        id = self.movies[self.index].getID()
        self.movie_obj = self.cinemagoer.get_movie(id)
        return self.movie_obj

    # Randomize the internal movie list
    def randomize(self):
        random.shuffle(self.movies)

    # Return the title of the current movie
    def title(self):
        return self.movies[self.index]["title"]
    
    # Return the current movie rating
    def rating(self):
        return self.movies[self.index]["rating"]

    # Return the URL for the cover image of the current movie
    def cover_url(self):
        return self.movie_obj["full-size cover url"]

    def plot_summary(self):
        return self.movie_obj["plot summary"]

    def genres(self):
        return self.movie_obj["genres"]