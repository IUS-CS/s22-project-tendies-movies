from flask import Flask, render_template
import os

app = Flask(__name__)

pictures = os.path.join('static','pics')

app.config['UPLOAD_FOLDER'] = pictures

# defining a route
@app.route("/", methods=['GET', 'POST', 'PUT']) # decorator
def home(): # route handler function
    # returning a response
    tempPic = os.path.join(app.config['UPLOAD_FOLDER'], 'pic1.jpg' )
    backPic = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg' )
    return render_template('index.html', user_image = tempPic, user_image1=backPic)


#debug mode on
app.run(debug = True)
