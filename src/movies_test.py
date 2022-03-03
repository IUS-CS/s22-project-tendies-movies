from Movie import Movie
import os
from imdb import Cinemagoer
from random import randint
ia = Cinemagoer()




top250movie = ia.get_top250_movies()
list = []


for i in range(len(top250movie)):
    list.append(Movie.convert(top250movie[i],i+1))



for m in list:
    print (m)

