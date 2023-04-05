# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 22:03:26 2023

@author: aneli
"""

from flask import Flask, render_template, request

app=Flask(__name__)
@app.route('/')
def root(): 
    return render_template('index.html')
if __name__ == '__main__': 
    app.run(host="localhost", port=8080, debug=True)