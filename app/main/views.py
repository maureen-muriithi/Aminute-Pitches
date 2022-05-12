from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required, current_user
from ..models import User, Pitch, Comment, Upvote, Downvote
from .forms import UpdateProfile,PitchForm,CommentForm
from .. import db

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

@main.route('/new_pitch', methods=['GET', 'POST'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        user_id = current_user._get_current_object().id
        post_obj = Pitch(post=post, title=title, category=category, user_id=user_id)
        post_obj.save()
        return redirect(url_for('main.index'))
    return render_template('pitch.html', form=form)


@main.route('/comment/<int:pitch_id>', methods=['GET', 'POST'])
@login_required
def comment(pitch_id):
    form = CommentForm()
    pitch = Pitch.query.get(pitch_id)
    user = User.query.all()
    comments = Comment.query.filter_by(pitch_id=pitch_id).all()
    if form.validate_on_submit():
        comment = form.comment.data
        pitch_id = pitch_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(
            comment=comment,
            pitch_id=pitch_id,
            user_id=user_id
        )
        new_comment.save()
        new_comments = [new_comment]
        print(new_comments)
        return redirect(url_for('.comment', pitch_id=pitch_id))
    return render_template('comment.html', form=form, pitch=pitch, comments=comments, user=user)

    