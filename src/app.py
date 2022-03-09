import os
from flask import Flask, render_template, request
from MovieClass import MovieClass
from imdb import Cinemagoer

movie = MovieClass()
movie.import_top250()
movie.randomize()

app = Flask(__name__)
pictures = os.path.join('static','pics') #load pictures folder to flask
app.config['UPLOAD_FOLDER'] = pictures

# defining a route
@app.route("/", methods=['GET', 'POST', 'PUT']) # decorator
def home(): # route handler function
    tempPic = os.path.join(app.config['UPLOAD_FOLDER'], 'pic1.jpg' ) #temp variable for sample pic
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    yesbackPic = os.path.join(app.config['UPLOAD_FOLDER'], 'yespic.jpg' ) #variable for yes_background image
    # get a movie
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

    return render_template('index.html', movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            background=backPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres()) 

@app.route("/western/", methods=['GET', 'POST', 'PUT']) # decorator
def western(): # route handler function
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    count = 0
    while (count != 1):
        movie.randomize()
        for i in movie.genres:
            if(i == "Western"):
                count = 1
    return render_template('no.html',  movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            background=backPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres())

@app.route("/drama/", methods=['GET', 'POST', 'PUT']) # decorator
def drama(): # route handler function
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    count = 0
    movie.randomize()
    while (count != 1):
        movie.randomize()
        for i in movie.genres:
            if(i == "Drama"):
                count = 1
    return render_template('no.html',  movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            background=backPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres())

@app.route("/war/", methods=['GET', 'POST', 'PUT']) # decorator
def war(): # route handler function
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    count = 0
    movie.randomize()
    while (count != 1):
        movie.randomize()
        for i in movie.genres():
            if(i == "War"):
                count = 1
                break
    return render_template('no.html',  movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            background=backPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres()) 

@app.route("/crime/", methods=['GET', 'POST', 'PUT']) # decorator
def crime(): # route handler function
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    count = 0
    movie.randomize()
    while (count != 1):
        movie.randomize()
        for i in movie.genres():
            if(i == "Crime"):
                count = 1
    return render_template('no.html',  movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            background=backPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres())  

@app.route("/fantasy/", methods=['GET', 'POST', 'PUT']) # decorator
def fantasy(): # route handler function
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    count = 0
    movie.randomize()
    while (count != 1):
        movie.randomize()
        for i in movie.genres():
            if(i == "Fantasy"):
                count = 1
    return render_template('no.html',  movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            background=backPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres())   

@app.route("/action/", methods=['GET', 'POST', 'PUT']) # decorator
def action(): # route handler function
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    count = 0
    movie.randomize()
    while (count != 1):
        movie.randomize()
        for i in movie.genres():
            if(i == "Action"):
                count = 1
    return render_template('no.html',  movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            background=backPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres())   

@app.route("/romance/", methods=['GET', 'POST', 'PUT']) # decorator
def romance(): # route handler function
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    count = 0
    movie.randomize()
    while (count != 1):
        movie.randomize()
        for i in movie.genres():
            if(i == "Romance"):
                count = 1
    return render_template('no.html',  movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            background=backPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres())   
@app.route("/history/", methods=['GET', 'POST', 'PUT']) # decorator
def history(): # route handler function
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    count = 0
    movie.randomize()
    while (count != 1):
        movie.randomize()
        for i in movie.genres():
            if(i == "History"):
                count = 1
    return render_template('no.html',  movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            background=backPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres())   

@app.route("/biography/", methods=['GET', 'POST', 'PUT']) # decorator
def biography(): # route handler function
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    count = 0
    movie.randomize()
    while (count != 1):
        movie.randomize()
        for i in movie.genres():
            if(i == "Biography"):
                count = 1
    return render_template('no.html',  movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            background=backPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres())    

@app.route("/scifi/", methods=['GET', 'POST', 'PUT']) # decorator
def scifi(): # route handler function
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    count = 0
    movie.randomize()
    while (count != 1):
        movie.randomize()
        for i in movie.genres():
            if(i == "Sci-Fi"):
                count = 1
    return render_template('no.html',  movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            background=backPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres())   

@app.route("/adventure/", methods=['GET', 'POST', 'PUT']) # decorator
def adventure(): # route handler function
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    count = 0
    movie.randomize()
    while (count != 1):
        movie.randomize()
        for i in movie.genres():
            if(i == "Adventure"):
                count = 1
    return render_template('no.html',  movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            background=backPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres())   

@app.route("/mystery/", methods=['GET', 'POST', 'PUT']) # decorator
def mystery(): # route handler function
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    count = 0
    movie.randomize()
    while (count != 1):
        movie.randomize()
        for i in movie.genres():
            if(i == "Mystery"):
                count = 1
    return render_template('no.html',  movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            background=backPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres())   

@app.route("/random/", methods=['GET', 'POST', 'PUT']) # decorator
def random(): # route handler function
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    movie.randomize()
    return render_template('no.html',  movie_title = movie.title(), 
            movie_rating = movie.rating(), user_image = movie.cover_url(), 
            background=backPic, movie_plot_summary = movie.plot_summary(),
            movie_genres = movie.genres())                  

#debug mode on
app.run(debug = True)

