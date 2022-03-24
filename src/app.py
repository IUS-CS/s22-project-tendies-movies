import os
import re
from flask import Flask, render_template, request
from MovieClass import MovieClass

movie = MovieClass()
movie.import_top250()
movie.randomize()

#prepare to run the app and load background images
app = Flask(__name__)
pictures = os.path.join('static','pics') #load pictures folder to flask
app.config['UPLOAD_FOLDER'] = pictures

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
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    yesbackPic = os.path.join(app.config['UPLOAD_FOLDER'], 'yespic.jpg' ) #variable for yes_background image
    # get a movie
    if request.method == 'POST':

        if request.form['action'] == 'Yes!':
            return movie_details('yes.html', yesbackPic)

        elif request.form['action'] == 'No.':
            #progress to next film in the movie list
            movie.next()
            return movie_details('no.html', backPic)
        
        else:
            genre = request.form['action']
            if genre == 'Any movie for me':
                genre = ''

            movie.select_genre([genre])
            movie.randomize()
            return movie_details('no.html', backPic)

    return movie_details('index.html', backPic)

#debug mode on
app.run(debug = True)