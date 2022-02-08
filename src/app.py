from flask import Flask, render_template, request
import os

app = Flask(__name__)

pictures = os.path.join('static','pics') #load pictures folder to flask

app.config['UPLOAD_FOLDER'] = pictures

# defining a route
@app.route("/", methods=['GET', 'POST', 'PUT']) # decorator
def home(): # route handler function
    # returning a response
    if request.method == 'POST':
        if request.form['submit_button'] == 'THING1':
            print ("THING1")
        elif request.form['submit_button'] == 'THING2':
            print ("THING2")
        else:
            pass # unknown
    tempPic = os.path.join(app.config['UPLOAD_FOLDER'], 'pic1.jpg' ) #temp variable for sample pic
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' ) #variable for background image
    return render_template('index.html', user_image = tempPic, user_image1=backPic) #return html, sample pic, and background picture


#debug mode on
app.run(debug = True)
