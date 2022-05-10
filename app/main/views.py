from flask import render_template,request,redirect,url_for
from . import main
# from ..requests import get_movies,get_movie,search_movie
# from .forms import ReviewForm
# from ..models import Review

@main.route('/')
def index():
    
    title = "Welcome to Aminute Pitches"
    heading = "Aminute Pitches"
    
    return render_template('index.html', title=title, heading=heading)