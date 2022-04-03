import flask
from flask import Flask,render_template,url_for,request,send_file,jsonify,make_response
import pickle
import numpy as np
import pandas as pd

import time
from threading import Timer
run = True

def generateCardRiskPosition():

    date = time.strftime('%Y%m%d')

    # ! Read history
    # file_name = ("../project-cs-tu-presure-matress/python/history/history-" + date + ".csv")
    file_name = ("../project-cs-tu-presure-matress/python/history/history-20220301.csv")
    raw_data = pd.read_csv(file_name, header=None)
    # print(raw_data)
    raw_pressure = raw_data[1]
    raw_class = raw_data[2]
    index = raw_pressure.index
    number_of_rows = len(index)

    



    riskList = ["บริเวณก้นกบและสะโพก"]

    # riskList
    innerHTML = ""
    for i in riskList:
        riskTag = (f'''<div class="row">
            <div class="card mt-10 card-green" style="margin-left: 40px;">
                <div class="card-body">
                    <i class="fa fa-plus" style="font-size: 30px;color: #089bab;" ></i>
                </div>
            </div>
            <p class="font-weight-bold" style="margin: auto auto auto 20px;">{i}</p>
        </div>''')
        innerHTML += riskTag

    return innerHTML


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

@app.route('/get_riskPosition')
def get_riskPosition():
    response = generateCardRiskPosition()
    return jsonify({
        "riskPositionTag":response
    })

#Second route : Use our model to make prediction - render the results page.
# @app.route('/predict', methods=['POST'])
# def predict():
        

if __name__ == '__main__':
	app.run(debug=True)