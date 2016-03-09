#!usr/bin/env python
# -*- coding: utf-8 -*-

'''
Docstring
**********
Title: RealPython Flask Hello World!
Author: Adeel Ahmad
Email: adeelahmad84@me.com

'''

__version__ = "0.1"

import unittest
from flask import Flask

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route("/")
@app.route("/hello")

# define the view using a function, which returns a string
def hello_world():
    return "Hello, World!"

# start the development server using the run() method
if __name__ == "__main__":
    app.run()