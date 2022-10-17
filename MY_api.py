from flask import Flask
import json
import requests
# import json
# import random

app = Flask(__name__)
app.debug= True

@app.route('/')
def hello():
    stud_det= {"name": "saurabh mehanti" , "student id":"200525033"}
    return stud_det

@app.route('/webhook' , methods=['POST', 'GET'])
def Hullo():
    one = {""}
