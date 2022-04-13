import os
import re
from flask import Flask, render_template, request
from MovieClass import MovieClass
from imdb import Cinemagoer

#initialize the movie class and randomize the internal list
movie = MovieClass()
movie.import_top250()
movie.randomize()

app = Flask(__name__)
pictures = os.path.join('static','pics') #load pictures folder to flask
app.config['UPLOAD_FOLDER'] = pictures

# Variables for active HTML and background for all
backPic = ""
currentHTML = ""
flavortext = ""

#Returns a render template with all the movie details that "movie" currently
#points to. Uses the passed html file and background. Used to make code
#easier to read.
def movie_details(html, bg):
    return render_template(html, movie_title = movie.title(), 
        movie_rating = movie.rating(), user_image = movie.cover_url(), 
        background = bg, movie_plot_summary = movie.plot_summary(),
        movie_genres = movie.genres())

# defining a route
@app.route("/", methods=['GET', 'POST', 'PUT']) # decorator
def home(): # route handler function
    #Default background picture
    backPic = os.path.join(pictures, 'background.jpg')
    #Yes back picture
    yesBackPic = os.path.join(pictures, 'yespic.jpg')

    # get a movie
    if request.method == 'POST':
        actionForm = request.form['action']

        if actionForm == 'Yes!':
            currentHTML = 'yes.html'
            backPic = os.path.join(pictures, 'yespic.jpg')
        
        elif actionForm == 'No.' or actionForm == 'Any movie for me':
            movie.next()
            return movie_details('no.html', backPic)
        
        elif actionForm == 'Any movie for me':
            backPic = os.path.join(pictures, 'background.jpg')
            return movie_details('no.html', backPic)

        else:
    
    return movie_details(currentHTML, backPic)
        
        
        if request.form['action'] == 'Action':
           backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
           findMovie('Action')
           return render_template('action.html',  movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            background=actionbackpic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres())#Find an action flick

        if request.form['action'] == 'Adventure':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('Adventure')
            return render_template('adventure.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=adventurebackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find an adventure flick

        if request.form['action'] == 'Animation':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('Animation')
            return render_template('animation.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=animationbackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find an animation flick

        if request.form['action'] == 'Biography':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('Biography')
            return render_template('biography.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=biographybackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find an adventure flick

        if request.form['action'] == 'Comedy':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('Comedy')
            return render_template('comedy.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=comedybackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find a comedy

        if request.form['action'] == 'Crime':
            findMovie('Crime')
            return render_template('crime.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=crimebackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find a comedy

        if request.form['action'] == 'Drama':
            findMovie('Drama')
            return render_template('drama.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=dramabackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find a drama

        if request.form['action'] == 'Family':
            findMovie('Family')
            return render_template('family.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=familybackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find a fantasy flick

        if request.form['action'] == 'Fantasy':
            findMovie('Fantasy')
            return render_template('fantasy.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=fantasybackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find a fantasy flick

        if request.form['action'] == 'Film-Noir':
            findMovie('Film-Noir')
            return render_template('filmnoir.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=noirbackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find a fantasy flick

        if request.form['action'] == 'History':
            findMovie('History')
            return render_template('history.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=historybackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find a history flick

        if request.form['action'] == 'Horror':
            findMovie('Horror')
            return render_template('horror.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=horrorbackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find a history flick

        if request.form['action'] == 'Musical':
            findMovie('Musical')
            return render_template('musical.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=musicalbackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find a history flick

        if request.form['action'] == 'Mystery':
            findMovie('Mystery')
            return render_template('mystery.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=mysterybackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find a history flick

        if request.form['action'] == 'Romance':
            findMovie('Romance')
            return render_template('romance.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=romancebackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())

        if request.form['action'] == 'Sci-Fi':
            findMovie('Sci-Fi')
            return render_template('scifi.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=scifibackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())

        if request.form['action'] == 'Thriller':
            findMovie('Thriller')
            return render_template('thriller.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=thrillerbackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())

        if request.form['action'] == 'War':
            findMovie('War')
            return render_template('war.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=warbackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())

        if request.form['action'] == 'Western':
            findMovie('Western')
            return render_template('western.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=westernbackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())

        if request.form['action'] == 'Any movie for me':
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
