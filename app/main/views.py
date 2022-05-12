from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required, current_user
from ..models import User, Pitch, Comment, Upvote, Downvote
from .forms import UpdateProfile,PitchForm,CommentForm
from .. import db, photos

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

@main.route('/like/<int:id>', methods=['POST', 'GET'])
@login_required
def upvote(id):
    pitch = Pitch.query.get(id)
    upvote = Upvote(pitch=pitch, upvote=1)
    upvote.save()
    return redirect(url_for('main.pitches'))


@main.route('/dislike/<int:id>', methods=['GET', 'POST'])
@login_required
def downvote(id):
    pitch = Pitch.query.get(id)
    downvote = Downvote(pitch=pitch, downvote=1)
    downvote.save()
    return redirect(url_for('main.pitches'))

@main.route('/user/<username>')
@login_required
def profile(username):
    username = current_user.username
    user_id = current_user._get_current_object().id
    user = User.query.filter_by(username=username).first()
    posts = Pitch.query.filter_by(user_id =user_id).all()
    if user is None:
        return ('not found')
    return render_template('profile/profile.html', user=user, posts=posts)




@main.route('/user/<name>/update_profile', methods=['POST', 'GET'])
@login_required
def updateprofile(name):
    form = UpdateProfile()
    user = User.query.filter_by(username=name).first()
    if user is None:
        error = 'The user does not exist'
    if form.validate_on_submit():
        user.bio = form.bio.data
        user.save()
        return redirect(url_for('.profile', name=name))
    return render_template('profile/update_profile.html', form=form)

@main.route('/user/<name>/update/pic',methods= ['POST'])
@login_required
def update_pic(name):
    user = User.query.filter_by(username = name).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',name=name))




    