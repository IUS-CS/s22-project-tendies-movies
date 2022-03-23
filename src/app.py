import os
import re
from flask import Flask, render_template, request
from MovieClass import MovieClass
from imdb import Cinemagoer

movie = MovieClass()
movie.import_top250()
movie.randomize()

app = Flask(__name__)
pictures = os.path.join('static','pics') #load pictures folder to flask
app.config['UPLOAD_FOLDER'] = pictures

def findMovie(i):
    movie.randomize()
    if i in movie.genres():
        return 0
    else:
        return findMovie(i)
    

# defining a route
@app.route("/", methods=['GET', 'POST', 'PUT']) # decorator
def home(): # route handler function
    tempPic = os.path.join(app.config['UPLOAD_FOLDER'], 'pic1.jpg' ) #temp variable for sample pic
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    yesbackPic = os.path.join(app.config['UPLOAD_FOLDER'], 'yespic.jpg' ) #variable for yes_background image
    # get a movie
    if request.method == 'POST':

        if request.form['action'] == 'Yes!':
            return render_template('yes.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            yes_background = yesbackPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres())

        if request.form['action'] == 'No.':
            movie.randomize()
            return render_template('no.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            background=backPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres())

        if request.form['action'] == 'Action':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('Action')
            return render_template('Action.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=backPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find an action flick

        if request.form['action'] == 'Adventure':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('Adventure')
            return render_template('no.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=backPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find an adventure flick

        if request.form['action'] == 'Animation':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('Animation')
            return render_template('no.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=backPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find an animation flick

        if request.form['action'] == 'Biography':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('Biography')
            return render_template('no.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=backPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find an adventure flick

        if request.form['action'] == 'Comedy':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('Comedy')
            return render_template('no.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=backPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find a comedy

        if request.form['action'] == 'Crime':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('Crime')
            return render_template('no.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=backPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find a comedy

        if request.form['action'] == 'Drama':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            count = 0
            findMovie('Drama')
            return render_template('no.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=backPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find a drama

        if request.form['action'] == 'Family':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('Family')
            return render_template('no.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=backPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find a fantasy flick

        if request.form['action'] == 'Fantasy':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('Fantasy')
            return render_template('no.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=backPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find a fantasy flick

        if request.form['action'] == 'Film-Noir':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('Film-Noir')
            return render_template('no.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=backPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find a fantasy flick

        if request.form['action'] == 'History':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('History')
            return render_template('no.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=backPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find a history flick

        if request.form['action'] == 'Horror':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('Horror')
            return render_template('no.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=backPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find a history flick

        if request.form['action'] == 'Mystery':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('Mystery')
            return render_template('no.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=backPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find a history flick

        if request.form['action'] == 'Romance':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('Romance')
            return render_template('no.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=backPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())

        if request.form['action'] == 'Sci-Fi':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('Sci-Fi')
            return render_template('no.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=backPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())

        
        if request.form['action'] == 'Thriller':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('Thriller')
            return render_template('no.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=backPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())

        if request.form['action'] == 'War':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('War')
            return render_template('no.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=backPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())

        if request.form['action'] == 'Western':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('Western')
            return render_template('no.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=backPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())

        if request.form['action'] == 'Any movie for me':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            movie.randomize()
            return render_template('no.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=backPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())

    return render_template('index.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            background=backPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres()) 

#debug mode on
app.run(debug = True)

