from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_required
# from .forms import ReviewForm
# from ..models import Review

@main.route('/')
def index():
    
    title = "Welcome to Aminute Pitches"
    heading = "Aminute Pitches"
    
    return render_template('index.html', title=title, heading=heading)