from flask import Flask, render_template, request
from Movie import Movie
import os

app = Flask(__name__)
pictures = os.path.join('static','pics') #load pictures folder to flask
app.config['UPLOAD_FOLDER'] = pictures

#list of movies, WIP TESTING
movies = []
movies.append(Movie())
movies[0].name = "test"
movies[0].image = os.path.join(app.config['UPLOAD_FOLDER'], 'movietest.jpg')

# defining a route
@app.route("/", methods=['GET', 'POST', 'PUT']) # decorator
def home(): # route handler function
    tempPic = os.path.join(app.config['UPLOAD_FOLDER'], 'pic1.jpg' ) #temp variable for sample pic
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image

    # Button handling
    if request.method == 'POST':
        #testing button return
        return render_template('index.html', user_image = movies[0].image, user_image1 = backPic)
    
    return render_template('index.html', user_image = tempPic, user_image1=backPic) #return html, sample pic, and background picture



#debug mode on
app.run(debug = True)