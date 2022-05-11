from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_required
# from .forms import ReviewForm
# from ..models import Review

@main.route('/')
def index():
    
    title = "Welcome to Aminute Pitches"
    # pitches = Pitch.query.all()
    # business = Pitch.query.filter_by(category = 'Business').all() 
    # meet_greet = Pitch.query.filter_by(category = 'Meet_greet').all()
    # interviews = Pitch.query.filter_by(category = 'Interviews').all()
    return render_template ('index.html', title = title)
    return render_template('index.html', title=title, business=business, meet_greet=meet_greet, interviews=interviews, pitches=pitches)
    