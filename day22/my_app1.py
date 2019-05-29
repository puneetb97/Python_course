# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 18:41:46 2019

@author: Puneet
"""

from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def default():
    message = 'hello world'
    return render_template('index.html',message=message)

if __name__ == "__main__":
    app.run()