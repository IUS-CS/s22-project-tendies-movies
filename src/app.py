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
# Consider these the default return settings
backPic = os.path.join(pictures, 'background.jpg')
currentHTML = 'index.html'
flavortext = ''

#Returns a render template with all the movie details that "movie" currently
#points to. Uses the passed html file and background. Used to make code
#easier to read.
def movie_details(html, bg, text):
    return render_template(html, movie_title = movie.title(), 
        movie_rating = movie.rating(), user_image = movie.cover_url(), 
        background = bg, movie_plot_summary = movie.plot_summary(),
        movie_genres = movie.genres(), flavor_text=text)

# defining a route
@app.route("/", methods=['GET', 'POST', 'PUT']) # decorator
def home(): # route handler function
    # Set the local variable definitions to match global
    global currentHTML
    global backPic
    global flavortext

    # Check if a movie or genre has been selected
    if request.method == 'POST':
        actionForm = request.form['action']

        # Make sure default background is selected, and html is 'yes'
        if actionForm == 'Yes!':
            currentHTML = 'yes.html'
            backPic = os.path.join(pictures, 'yespic.jpg')
        
        # Load next movie
        # The html document to load should already be in the currentHTML var
        elif actionForm == 'No.':
            movie.next()
        
        # Don't need to load next movie, since the current one is the first one
        # Back sure background is set to default and html is 'no'
        elif actionForm == 'Any movie for me':
            currentHTML = 'no.html'
            backPic = os.path.join(pictures, 'background.jpg')

        # reset to default - index values
        elif actionForm == 'Different genre' or actionForm == 'New flick':
            currentHTML = 'index.html'
            backPic = os.path.join(pictures, 'background.jpg')

        # If we get to here then a specific genre has been selected
        # The 'actionForm' variable contains the string name of that genre
        # we use this to edit the flavortext and find the right background
        else:
            # Change to lowercase for ease of use
            actionForm = actionForm.lower()
            # Update the movie list to contain only the selected genre
            movie.select_genre(actionForm)
            movie.randomize()

            currentHTML = "genre_selected.html"
            backPic = os.path.join(pictures, (actionForm + ".jpg"))
            flavortext = "Is this the " + actionForm + " you're looking for?"

    return movie_details(currentHTML, backPic, flavortext)

#debug mode on
app.run(debug = True)