import flask
from flask import Flask,render_template,url_for,request,send_file
import pickle
import numpy as np

import time
from threading import Timer
run = True

#Initialize the useless part of the base64 encoded image.
init_Base64 = 21;

#Our dictionary
label_dict = {0:'Cat', 1:'Giraffe', 2:'Sheep', 3:'Bat', 4:'Octopus', 5:'Camel'}


#Initializing the Default Graph (prevent errors)
# graph = tf.get_default_graph()

# Use pickle to load in the pre-trained model.
# with open(f'model_cnn.pkl', 'rb') as f:
#         model = pickle.load(f)

#Initializing new Flask instance. Find the html template in "templates".
app = flask.Flask(__name__, template_folder='templates')

#First route : Render the initial drawing template
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/get_image')
def get_image():
    # if request.args.get('type') == '1':
    filename = './static/temp/test.gif'
    # else:
    #    filename = 'error.gif'
    return send_file(filename, mimetype='image/gif')

@app.route('/get_image16')
def get_image16():
    # if request.args.get('type') == '1':
    filename = './static/temp16/test.gif'
    # else:
    #    filename = 'error.gif'
    return send_file(filename, mimetype='image/gif')


#Second route : Use our model to make prediction - render the results page.
# @app.route('/predict', methods=['POST'])
# def predict():
        

if __name__ == '__main__':
	app.run(debug=True)