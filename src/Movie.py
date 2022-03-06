class Movie:
    #Basic constructor for movie elements

    def __init__(self):
        self.id = 0
        self.title = ""
        self.description = ""
        self.image = ""
        self.genres = []
        self.imdb_rating = 0
        self.rank = 0

    @staticmethod
    def convert(cinemagoer_movie, rank = 0):
        m = Movie()
        m.id = cinemagoer_movie.getID()
        m.title = cinemagoer_movie['title']
        m.description = cinemagoer_movie['plot summary']
        m.image = cinemagoer_movie['full-size cover url']
        m.genres = cinemagoer_movie['genres']
        m.imdb_rating = cinemagoer_movie['rating']
        m.rank = rank
        return m

    #def __repr__(self):
    #   return str(self)

    def __str__(self):
        return "Movie(" + \
               "rank=" + str(self.rank) + \
               ", id=" + str(self.id) + \
               ", title=\"" + str(self.title) + "\"" + \
               ", description=" + str(self.description) + \
               ", image=" + str(self.image) + \
               ", genres=" + str(self.genres) + \
               ", imdb_rating=" + str(self.imdb_rating) + ")"
