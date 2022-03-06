from random import randint
from flask import Flask, render_template, request
from Movie import Movie
import os
from imdb import Cinemagoer

# create an instance of the Cinemagoer class
ia = Cinemagoer()

# get a movie
movie = ia.get_top250_movies()

#random_Movie=randint(0,249)
#title = movie[random_Movie]['title']
#rating = movie[random_Movie]['rating']
# specific id number to retrieve movie object from cinemagoer
#id = movie[random_Movie].getID()
#cinemagoer specific movie object with access to more data fields (like cover url, plot summary, genres, etc)
#cinemagoer_movie_object = ia.get_movie(id)
#url = cinemagoer_movie_object['full-size cover url']
#TODO fix formatting
#plot_summary = cinemagoer_movie_object['plot summary']
#TODO fix formatting
#genres = cinemagoer_movie_object['genres']


app = Flask(__name__)
pictures = os.path.join('static','pics') #load pictures folder to flask
app.config['UPLOAD_FOLDER'] = pictures

# defining a route
@app.route("/", methods=['GET', 'POST', 'PUT']) # decorator
def home(): # route handler function
    tempPic = os.path.join(app.config['UPLOAD_FOLDER'], 'pic1.jpg' ) #temp variable for sample pic
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    yesbackPic = os.path.join(app.config['UPLOAD_FOLDER'], 'yespic.jpg' ) #variable for yes_background image
    random_Movie=randint(0,249)
    title = movie[random_Movie]['title']
    rating = movie[random_Movie]['rating']
    # specific id number to retrieve movie object from cinemagoer
    id = movie[random_Movie].getID()
    #cinemagoer specific movie object with access to more data fields (like cover url, plot summary, genres, etc)
    cinemagoer_movie_object = ia.get_movie(id)
    url = cinemagoer_movie_object['full-size cover url']
    #TODO fix formatting
    plot_summary = cinemagoer_movie_object['plot summary']
    #TODO fix formatting
    genres = cinemagoer_movie_object['genres']
    # Button handling
    if request.method == 'POST':
        #testing button return
        if request.form['action'] == 'Yes!':
            return render_template('yes.html', yes_title=title, movie_rating = rating, user_image = url, yes_background = yesbackPic , movie_plot_summary = plot_summary, movie_genres = genres)
        if request.form['action'] == 'No.':
            random_Movie=randint(0,249)
            title = movie[random_Movie]['title']
            rating = movie[random_Movie]['rating']
            # specific id number to retrieve movie object from cinemagoer
            id = movie[random_Movie].getID()
            #cinemagoer specific movie object with access to more data fields (like cover url, plot summary, genres, etc)
            cinemagoer_movie_object = ia.get_movie(id)
            url = cinemagoer_movie_object['full-size cover url']
            #TODO fix formatting
            plot_summary = cinemagoer_movie_object['plot summary']
            #TODO fix formatting
            genres = cinemagoer_movie_object['genres']
            return render_template('no.html', movie_title=title, movie_rating = rating, user_image = url, background=backPic , movie_plot_summary = plot_summary, movie_genres = genres)
    
    return render_template('index.html', movie_title=title, movie_rating = rating, user_image = url, background=backPic , movie_plot_summary = plot_summary, movie_genres = genres) #return html, sample pic, and background picture



#debug mode on
app.run(debug = True)

