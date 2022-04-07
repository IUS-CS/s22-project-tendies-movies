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
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    yesbackPic = os.path.join(app.config['UPLOAD_FOLDER'], 'yespic.jpg' ) #variable for yes_background image
    scifibackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'scifi.jpg' )
    actionbackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'action.jpg' )
    romancebackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'romance.jpg' )
    adventurebackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'adventure.jpg' )
    animationbackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'animation.jpg' )
    biographybackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'biography.jpg' )
    comedybackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'comedy.jpg' )
    crimebackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'crime.jpg' )
    dramabackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'drama.jpg' )
    familybackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'family.jpg' )
    fantasybackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'fantasy.jpg' )
    noirbackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'noir.jpg' )
    historybackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'history.jpg' )
    horrorbackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'horror.jpg' )
    musicalbackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'musical.jpg' )
    mysterybackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'mystery.jpg' )
    thrillerbackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'thriller.jpg' )
    warbackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'war.jpg' )
    westernbackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'western.jpg' )

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

@app.route("/yes", methods=['GET', 'POST', 'PUT']) # decorator
def yes(): # route handler function
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image

    if request.method == 'POST':

        if request.form['action'] == 'Yes!':
            return render_template('index.html', background = backPic)

# defining action route
@app.route("/action", methods=['GET', 'POST', 'PUT']) 
def action(): # route handler function
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    yesbackPic = os.path.join(app.config['UPLOAD_FOLDER'], 'yespic.jpg' ) #variable for yes_background image
    actionbackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'action.jpg' )
    # get a movie

    if request.method == 'POST':

        if request.form['action'] == 'Yes!':
            return render_template('yes.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            yes_background = yesbackPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres())

        if request.form['action'] == 'No.':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('Action')
            return render_template('action.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=actionbackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find an action flick

        if request.form['action'] == "Different genre":
            return render_template('index.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            background=backPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres()) 

@app.route("/adventure", methods=['GET', 'POST', 'PUT']) 
def adventure(): # route handler function
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    yesbackPic = os.path.join(app.config['UPLOAD_FOLDER'], 'yespic.jpg' ) #variable for yes_background image
    adventurebackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'adventure.jpg' )
    # get a movie

    if request.method == 'POST':

        if request.form['action'] == 'Yes!':
            return render_template('yes.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            yes_background = yesbackPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres())

        if request.form['action'] == 'No.':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('Adventure')
            return render_template('adventure.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=adventurebackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find an action flick

        if request.form['action'] == "Different genre":
            return render_template('index.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            background=backPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres()) 

@app.route("/animation", methods=['GET', 'POST', 'PUT']) 
def animation(): # route handler function
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    yesbackPic = os.path.join(app.config['UPLOAD_FOLDER'], 'yespic.jpg' ) #variable for yes_background image
    animationbackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'animation.jpg' )
    # get a movie

    if request.method == 'POST':

        if request.form['action'] == 'Yes!':
            return render_template('yes.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            yes_background = yesbackPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres())

        if request.form['action'] == 'No.':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('Animation')
            return render_template('animation.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=animationbackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find an action flick

        if request.form['action'] == "Different genre":
            return render_template('index.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            background=backPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres()) 

@app.route("/biography", methods=['GET', 'POST', 'PUT']) 
def biography(): # route handler function
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    yesbackPic = os.path.join(app.config['UPLOAD_FOLDER'], 'yespic.jpg' ) #variable for yes_background image
    biographybackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'biography.jpg' )
    # get a movie

    if request.method == 'POST':

        if request.form['action'] == 'Yes!':
            return render_template('yes.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            yes_background = yesbackPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres())

        if request.form['action'] == 'No.':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('Biography')
            return render_template('biography.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=biographybackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find an action flick

        if request.form['action'] == "Different genre":
            return render_template('index.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            background=backPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres()) 

@app.route("/comedy", methods=['GET', 'POST', 'PUT']) 
def comedy(): # route handler function
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    yesbackPic = os.path.join(app.config['UPLOAD_FOLDER'], 'yespic.jpg' ) #variable for yes_background image
    comedybackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'comedy.jpg' )
    # get a movie

    if request.method == 'POST':

        if request.form['action'] == 'Yes!':
            return render_template('yes.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            yes_background = yesbackPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres())

        if request.form['action'] == 'No.':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('Comedy')
            return render_template('comedy.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=comedybackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find an action flick

        if request.form['action'] == "Different genre":
            return render_template('index.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            background=backPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres()) 

@app.route("/crime", methods=['GET', 'POST', 'PUT']) 
def crime(): # route handler function
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    yesbackPic = os.path.join(app.config['UPLOAD_FOLDER'], 'yespic.jpg' ) #variable for yes_background image
    crimebackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'crime.jpg' )
    # get a movie

    if request.method == 'POST':

        if request.form['action'] == 'Yes!':
            return render_template('yes.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            yes_background = yesbackPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres())

        if request.form['action'] == 'No.':
            findMovie('Crime')
            return render_template('crime.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=crimebackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find an action flick

        if request.form['action'] == "Different genre":
            return render_template('index.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            background=backPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres()) 

@app.route("/drama", methods=['GET', 'POST', 'PUT']) 
def drama(): # route handler function
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    yesbackPic = os.path.join(app.config['UPLOAD_FOLDER'], 'yespic.jpg' ) #variable for yes_background image
    dramabackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'drama.jpg' )
    # get a movie

    if request.method == 'POST':

        if request.form['action'] == 'Yes!':
            return render_template('yes.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            yes_background = yesbackPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres())

        if request.form['action'] == 'No.':
            findMovie('Drama')
            return render_template('drama.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=dramabackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find an action flick

        if request.form['action'] == "Different genre":
            return render_template('index.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            background=backPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres()) 

@app.route("/family", methods=['GET', 'POST', 'PUT']) 
def family(): # route handler function
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    yesbackPic = os.path.join(app.config['UPLOAD_FOLDER'], 'yespic.jpg' ) #variable for yes_background image
    familybackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'family.jpg' )
    # get a movie

    if request.method == 'POST':

        if request.form['action'] == 'Yes!':
            return render_template('yes.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            yes_background = yesbackPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres())

        if request.form['action'] == 'No.':
            findMovie('Family')
            return render_template('family.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=familybackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find an action flick

        if request.form['action'] == "Different genre":
            return render_template('index.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            background=backPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres()) 

@app.route("/fantasy", methods=['GET', 'POST', 'PUT']) 
def fantasy(): # route handler function
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    yesbackPic = os.path.join(app.config['UPLOAD_FOLDER'], 'yespic.jpg' ) #variable for yes_background image
    fantasybackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'fantasy.jpg' )
    # get a movie

    if request.method == 'POST':

        if request.form['action'] == 'Yes!':
            return render_template('yes.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            yes_background = yesbackPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres())

        if request.form['action'] == 'No.':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('Fantasy')
            return render_template('fantasy.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=fantasybackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find an action flick

        if request.form['action'] == "Different genre":
            return render_template('index.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            background=backPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres()) 

@app.route("/filmnoir", methods=['GET', 'POST', 'PUT']) 
def noir(): # route handler function
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    yesbackPic = os.path.join(app.config['UPLOAD_FOLDER'], 'yespic.jpg' ) #variable for yes_background image
    noirbackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'noir.jpg' )
    # get a movie

    if request.method == 'POST':

        if request.form['action'] == 'Yes!':
            return render_template('yes.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            yes_background = yesbackPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres())

        if request.form['action'] == 'No.':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('Film-Noir')
            return render_template('filmnoir.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=noirbackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find an action flick

        if request.form['action'] == "Different genre":
            return render_template('index.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            background=backPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres()) 

@app.route("/history", methods=['GET', 'POST', 'PUT']) 
def history(): # route handler function
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    yesbackPic = os.path.join(app.config['UPLOAD_FOLDER'], 'yespic.jpg' ) #variable for yes_background image
    historybackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'history.jpg' )
    # get a movie

    if request.method == 'POST':

        if request.form['action'] == 'Yes!':
            return render_template('yes.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            yes_background = yesbackPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres())

        if request.form['action'] == 'No.':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('History')
            return render_template('history.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=historybackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find an action flick

        if request.form['action'] == "Different genre":
            return render_template('index.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            background=backPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres()) 

@app.route("/horror", methods=['GET', 'POST', 'PUT']) 
def horror(): # route handler function
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    yesbackPic = os.path.join(app.config['UPLOAD_FOLDER'], 'yespic.jpg' ) #variable for yes_background image
    horrorbackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'horror.jpg' )
    # get a movie

    if request.method == 'POST':

        if request.form['action'] == 'Yes!':
            return render_template('yes.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            yes_background = yesbackPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres())

        if request.form['action'] == 'No.':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('Horror')
            return render_template('horror.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=horrorbackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find an action flick

        if request.form['action'] == "Different genre":
            return render_template('index.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            background=backPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres()) 

@app.route("/musical", methods=['GET', 'POST', 'PUT']) 
def musical(): # route handler function
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    yesbackPic = os.path.join(app.config['UPLOAD_FOLDER'], 'yespic.jpg' ) #variable for yes_background image
    musicalbackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'musical.jpg' )
    # get a movie

    if request.method == 'POST':

        if request.form['action'] == 'Yes!':
            return render_template('yes.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            yes_background = yesbackPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres())

        if request.form['action'] == 'No.':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('Musical')
            return render_template('musical.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=musicalbackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find an action flick

        if request.form['action'] == "Different genre":
            return render_template('index.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            background=backPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres()) 

@app.route("/mystery", methods=['GET', 'POST', 'PUT']) 
def mystery(): # route handler function
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    yesbackPic = os.path.join(app.config['UPLOAD_FOLDER'], 'yespic.jpg' ) #variable for yes_background image
    mysterybackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'mystery.jpg' )
    # get a movie

    if request.method == 'POST':

        if request.form['action'] == 'Yes!':
            return render_template('yes.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            yes_background = yesbackPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres())

        if request.form['action'] == 'No.':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('Mystery')
            return render_template('mystery.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=mysterybackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find an action flick

        if request.form['action'] == "Different genre":
            return render_template('index.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            background=backPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres()) 

@app.route("/thriller", methods=['GET', 'POST', 'PUT']) 
def thriller(): # route handler function
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    yesbackPic = os.path.join(app.config['UPLOAD_FOLDER'], 'yespic.jpg' ) #variable for yes_background image
    thrillerbackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'thriller.jpg' )
    # get a movie

    if request.method == 'POST':

        if request.form['action'] == 'Yes!':
            return render_template('yes.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            yes_background = yesbackPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres())

        if request.form['action'] == 'No.':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('Thriller')
            return render_template('thriller.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=thrillerbackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find an action flick

        if request.form['action'] == "Different genre":
            return render_template('index.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            background=backPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres()) 

@app.route("/war", methods=['GET', 'POST', 'PUT']) 
def war(): # route handler function
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    yesbackPic = os.path.join(app.config['UPLOAD_FOLDER'], 'yespic.jpg' ) #variable for yes_background image
    warbackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'war.jpg' )
    # get a movie

    if request.method == 'POST':

        if request.form['action'] == 'Yes!':
            return render_template('yes.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            yes_background = yesbackPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres())

        if request.form['action'] == 'No.':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('War')
            return render_template('war.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=warbackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find an action flick

        if request.form['action'] == "Different genre":
            return render_template('index.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            background=backPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres()) 

@app.route("/western", methods=['GET', 'POST', 'PUT']) 
def western(): # route handler function
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    yesbackPic = os.path.join(app.config['UPLOAD_FOLDER'], 'yespic.jpg' ) #variable for yes_background image
    westernbackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'western.jpg' )
    # get a movie

    if request.method == 'POST':

        if request.form['action'] == 'Yes!':
            return render_template('yes.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            yes_background = yesbackPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres())

        if request.form['action'] == 'No.':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('Western')
            return render_template('western.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=westernbackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find an action flick

        if request.form['action'] == "Different genre":
            return render_template('index.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            background=backPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres()) 


@app.route("/romance", methods=['GET', 'POST', 'PUT']) 
def romance(): # route handler function
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    yesbackPic = os.path.join(app.config['UPLOAD_FOLDER'], 'yespic.jpg' ) #variable for yes_background image
    romancebackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'romance.jpg' )
    # get a movie

    if request.method == 'POST':

        if request.form['action'] == 'Yes!':
            return render_template('yes.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            yes_background = yesbackPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres())

        if request.form['action'] == 'No.':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('Romance')
            return render_template('romance.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=romancebackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find an action flick

        if request.form['action'] == "Different genre":
            return render_template('index.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            background=backPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres()) 

@app.route("/scifi", methods=['GET', 'POST', 'PUT']) 
def scifi(): # route handler function
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    yesbackPic = os.path.join(app.config['UPLOAD_FOLDER'], 'yespic.jpg' ) #variable for yes_background image
    scifibackpic = os.path.join(app.config['UPLOAD_FOLDER'], 'scifi.jpg' )
    # get a movie

    if request.method == 'POST':

        if request.form['action'] == 'Yes!':
            return render_template('yes.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            yes_background = yesbackPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres())

        if request.form['action'] == 'No.':
            backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
            findMovie('Sci-Fi')
            return render_template('scifi.html',  movie_title = movie.title(), 
                movie_rating = movie.rating(), user_image = movie.cover_url(), 
                background=scifibackpic, movie_plot_summary = movie.plot_summary(),
                movie_genres = movie.genres())#Find an action flick

        if request.form['action'] == "Different genre":
            return render_template('index.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            background=backPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres()) 


#debug mode on
app.run(debug = True)
