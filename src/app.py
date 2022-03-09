import os
from flask import Flask, render_template, request
from MovieClass import MovieClass
from imdb import Cinemagoer

movie = MovieClass()
movie.import_top250()
movie.randomize()

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
            return render_template('yes.html', movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                yes_background = yesbackPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())
        if request.form['action'] == 'No.':
            movie.randomize()
            return render_template('no.html', movie_title=movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), background=backPic)
    
    return render_template('index.html', movie_title=movie.title(), movie_rating = movie.rating(), 
        user_image = movie.cover_url(), background=backPic) #return html, sample pic, and background picture

#debug mode on
app.run(debug = True)