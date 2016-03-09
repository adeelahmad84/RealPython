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
# dynamic route
@app.route("/test/<search_query>")
def search(search_query):
    return search_query

@app.route("/integer/<int:value>")
def int_type(value):
    print value + 1
    return "correct"

@app.route("/float/<float:value>")
def float_type(value):
        print value + 1
        return "correct"

# dynamic route that accepts slashes
@app.route("/path/<path:value>")
def path_type(value):
        print value
        return "correct"

# define the view using a function, which returns a string
def hello_world():
    return "Hello, World!"

@app.route("/name/<name>")
def  index(name):
    if name.lower() == "michael" :
	return "Hello, {}".format(name), 200
    else:
	return "Not Found", 404

app.config["DEBUG"] = True

# start the development server using the run() method
if __name__ == "__main__":
    app.run()
    import doctest
    doctest.testmod()
    class MyTest(unittest.TestCase):
        def test(self):
            self.assertEqual(main(), )