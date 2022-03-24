import os
import re
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

#Returns a render template with all the movie details that "movie" currently
#points to. Uses the passed html file and background.
def movie_details(html, background):
    return render_template(html, movie_title = movie.title(), 
        movie_rating = movie.rating(), user_image = movie.cover_url(), 
        background=background, movie_plot_summary = movie.plot_summary(),
        movie_genres = movie.genres())

# defining a route
@app.route("/", methods=['GET', 'POST', 'PUT']) # decorator
def home(): # route handler function
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
            count = 0
            while (count != 1):
                movie.randomize()
                for i in movie.genres():
                    if(i == "Action"):
                        count = 1
            return render_template('no.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=backPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find an action flick

        if request.form['action'] == 'Adventure':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            count = 0
            while (count != 1):
                movie.randomize()
                for i in movie.genres():
                    if(i == "Adventure"):
                        count = 1
            return render_template('no.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=backPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find an adventure flick

        if request.form['action'] == 'Animation':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            count = 0
            while (count != 1):
                movie.randomize()
                for i in movie.genres():
                    if(i == "Animation"):
                        count = 1
            return render_template('no.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=backPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find an animation flick

        if request.form['action'] == 'Biography':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            count = 0
            while (count != 1):
                movie.randomize()
                for i in movie.genres():
                    if(i == "Biography"):
                        count = 1
            return render_template('no.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=backPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find an adventure flick

        if request.form['action'] == 'Comedy':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            count = 0
            while (count != 1):
                movie.randomize()
                for i in movie.genres():
                    if(i == "Comedy"):
                        count = 1
            return render_template('no.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=backPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find a comedy

        if request.form['action'] == 'Crime':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            count = 0
            while (count != 1):
                movie.randomize()
                for i in movie.genres():
                    if(i == "Crime"):
                        count = 1
            return render_template('no.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=backPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find a comedy

        if request.form['action'] == 'Drama':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            count = 0
            while (count != 1):
                movie.randomize()
                for i in movie.genres():
                    if(i == "Drama"):
                        count = 1
            return render_template('no.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=backPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find a drama

        if request.form['action'] == 'Family':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            count = 0
            while (count != 1):
                movie.randomize()
                for i in movie.genres():
                    if(i == "Family"):
                        count = 1
            return render_template('no.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=backPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find a fantasy flick

        if request.form['action'] == 'Fantasy':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            count = 0
            while (count != 1):
                movie.randomize()
                for i in movie.genres():
                    if(i == "Fantasy"):
                        count = 1
            return render_template('no.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=backPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find a fantasy flick

        if request.form['action'] == 'Film-Noir':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            count = 0
            while (count != 1):
                movie.randomize()
                for i in movie.genres():
                    if(i == "Film-Noir"):
                        count = 1
            return render_template('no.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=backPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find a fantasy flick

        if request.form['action'] == 'History':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            count = 0
            while (count != 1):
                movie.randomize()
                for i in movie.genres():
                    if(i == "History"):
                        count = 1
            return render_template('no.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=backPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find a history flick

        if request.form['action'] == 'Horror':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            count = 0
            while (count != 1):
                movie.randomize()
                for i in movie.genres():
                    if(i == "Horror"):
                        count = 1
            return render_template('no.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=backPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find a history flick

        if request.form['action'] == 'Mystery':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            count = 0
            while (count != 1):
                movie.randomize()
                for i in movie.genres():
                    if(i == "Mystery"):
                        count = 1
            return render_template('no.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=backPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find a history flick

        if request.form['action'] == 'Romance':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            count = 0
            while (count != 1):
                movie.randomize()
                for i in movie.genres():
                    if(i == "Romance"):
                        count = 1
            return render_template('no.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=backPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())

        if request.form['action'] == 'Sci-Fi':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            count = 0
            while (count != 1):
                movie.randomize()
                for i in movie.genres():
                    if(i == "Sci-Fi"):
                        count = 1
            return render_template('no.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=backPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())

        
        if request.form['action'] == 'Thriller':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            count = 0
            while (count != 1):
                movie.randomize()
                for i in movie.genres():
                    if(i == "Thriller"):
                        count = 1
            return render_template('no.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=backPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())

        if request.form['action'] == 'War':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            count = 0
            while (count != 1):
                movie.randomize()
                for i in movie.genres():
                    if(i == "War"):
                        count = 1
            return render_template('no.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=backPic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())

        if request.form['action'] == 'Western':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            count = 0
            while (count != 1):
                movie.randomize()
                for i in movie.genres():
                    if(i == "Western"):
                        count = 1
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

#Disable to use Behave testing
app.run(debug = True)