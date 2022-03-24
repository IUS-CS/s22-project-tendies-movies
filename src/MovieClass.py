import random
from imdb import Cinemagoer

class MovieClass:
    #Basic constructor for movie elements
    def __init__(self):
        self.movies = []
        self.index = 0
        self.cinemagoer = Cinemagoer()
        self.movie_obj = None
        self.selected_genre = []

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
        self.selected_genre = genres
        
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

            #After incrementing, we need to make sure the current movie
            #is of the selected genres.
            self._verify_genre()
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
        self._verify_genre()

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

    # Verify the current movie is actually part of the selected genres list
    def _verify_genre(self):
        if self.selected_genre != []:
                flag = False
                for genre in self.selected_genre:
                    #If the genre IS selected, then exit the loop
                    if genre in self.genres():
                        flag = True
                        break
                #If we never selected any of the genres, then increment    
                if not flag:
                    self.next()