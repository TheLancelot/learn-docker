# print("HIIIIIIIII") can just run this as it is, and it will print in the terminal
#but usually we make apis and then expose those apis

## flask app for hello world
from flask import Flask
import numpy as np
import pandas as pd

app=Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return "Hello World"



if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)