from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required, current_user
from ..models import User, Pitch, Comment, Upvote, Downvote
from .forms import UpdateProfile,PitchForm,CommentForm
from .. import db,photos

@main.route('/')
def index():
    
    title = "Welcome to Aminute Pitches"
    pitches = Pitch.query.all()
    business = Pitch.query.filter_by(category = 'Business').all() 
    meet_greet = Pitch.query.filter_by(category = 'Meet_greet').all()
    interviews = Pitch.query.filter_by(category = 'Interviews').all()
    return render_template('index.html', title=title, business=business, meet_greet=meet_greet, interviews=interviews, pitches=pitches)

@main.route('/pitches')
@login_required
def pitches():
    pitches = Pitch.query.all()
    upvote = Upvote.query.all()
    user = current_user
    return render_template('view_pitches.html', pitches=pitches, upvote=upvote, user=user)
    