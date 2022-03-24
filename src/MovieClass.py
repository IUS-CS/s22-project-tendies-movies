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

    # Import a list of movies into the class
    def replace(self, movie_list):
        self.movies = movie_list
        self.index = 0

    # Takes a list of genres and removes all movies that are not
    # any of those genres
    def select_genre(self, genres):
        selected_movies = []
        
        #Find all movies with the provided genres
        for movie in self.movies:
            for genre in genres:
                if genre in self.genres():
                    selected_movies.append(movie)
                    break  

        self.replace(selected_movies)
        print(selected_movies)

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
        #otherwise, wrap around to 0
            self.index = 0

    # Return the movie object of the current movie
    def movie_object(self):
        #If there is not a movie object for the current film, make one
        if self.movie_obj == None:
            print("Index: " + str(self.index) + "\nLength: " + str(len(self.movies)))

            id = self.movies[self.index].getID()
            self.movie_obj = self.cinemagoer.get_movie(id)
        return self.movie_obj

    # Randomize the internal movie list
    def randomize(self):
        random.shuffle(self.movies)

    # Return the title of the current movie
    def title(self):
        return self.movie_object()["title"]

    # Return the current movie rating
    def rating(self):
        return self.movie_object()["rating"]

    # Return the URL for the cover image of the current movie
    def cover_url(self):
        return self.movie_object()["full-size cover url"]

    def plot_summary(self):
        return self.movie_object()["plot summary"]

    def genres(self):
        return self.movie_object()["genres"] 
