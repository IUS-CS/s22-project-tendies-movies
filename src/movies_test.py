from Movie import Movie
import os
from imdb import Cinemagoer
from random import randint
ia = Cinemagoer()




top250movie = ia.get_top250_movies()
list = []

for i in range(len(top250movie)):
    id = top250movie[i].getID()
    m = ia.get_movie(id)
    list.append(Movie.convert(m,i+1))



for m in list:
    print (m)

