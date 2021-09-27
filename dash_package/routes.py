from flask import render_template

from dash_package import server

@server.route('/')
def index():
    return 'HOME PAGE'

@server.route('/stuff')
def render_stuff():
    return 'stuff'
