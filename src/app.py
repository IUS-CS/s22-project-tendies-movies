import random
from flask import Flask, render_template, request
import os
from imdb import Cinemagoer

# create an instance of the Cinemagoer class
ia = Cinemagoer()

# get the list of top 250 movies
movies = ia.get_top250_movies()
# randomize movies
random.shuffle(movies)
# keeps track of our random list
movie_index = 0

# Individual variables for movie details
title = movies[movie_index]['title']
rating = movies[movie_index]['rating']
# specific id number to retrieve movie object from cinemagoer
id = movies[movie_index].getID()
# cinemagoer specific movie object with access to more data fields 
# (like cover url, plot summary, genres, etc)
cinemagoer = ia.get_movie(id)
url = cinemagoer['full-size cover url']
plot_summary = cinemagoer['plot summary']
genres = cinemagoer['genres']

#prepare to run the app and load background images
app = Flask(__name__)
pictures = os.path.join('static','pics') #load pictures folder to flask
app.config['UPLOAD_FOLDER'] = pictures

# defining a route
@app.route("/", methods=['GET', 'POST', 'PUT']) # decorator
def home(): # route handler function
    tempPic = os.path.join(app.config['UPLOAD_FOLDER'], 'pic1.jpg' ) #temp variable for sample pic
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    yesbackPic = os.path.join(app.config['UPLOAD_FOLDER'], 'yespic.jpg' ) #variable for yes_background image

    # Button handling
    if request.method == 'POST':
        #testing button return
        if request.form['action'] == 'Yes!':
            return render_template('yes.html', movie_title=title, movie_rating = rating, user_image = url, yes_background = yesbackPic , movie_plot_summary = plot_summary, movie_genres = genres)
        if request.form['action'] == 'No.':
            return render_template('no.html', movie_title=title, movie_rating = rating, user_image = url, background=backPic)
    
    return render_template('index.html', movie_title=title, movie_rating = rating, user_image = url, background=backPic) #return html, sample pic, and background picture

#debug mode turned off, needed to test with Behave
#app.run(debug = True)