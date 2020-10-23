from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User, Pitch
from .forms import DeleteUser, UpdateProfile, PitchForm
from .. import db, photos
from flask_login import login_required




@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')


@main.route('/user/<uname>', methods = ['GET', 'POST'])
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    form = DeleteUser()
    

    if user is None:
        abort(404)
    elif form.validate_on_submit():
        db.session.delete(user)
        db.session.commit()

        return redirect(url_for('main.index'))
    else:

        return render_template('profile/profile.html', user = user, delete = form)

@main.route('/user/<uname>/update', methods = ['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    

    if user is None:
        abort(404)

    form = UpdateProfile()


    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname = user.username))
    
    return render_template('profile/update.html', form = form)

@main.route('/user/<uname>/update/pic', methods  = ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname = uname))

@main.route('/category/<category>')
def show_pitches(category):
    '''
    function that will show the pitches under a certain category
    '''
    pitches = Pitch.get_all_pitches()
    catego = category
    spec_pitches = []
    categ_name = category.split('-')
    categ = " ".join(categ_name).title()

    
    for pitch in pitches:
        if pitch.category_pitch == catego:
            spec_pitches.insert(0, pitch)
    


    return render_template('pitches_for_cat.html', category = catego, categ_formatted = categ, pitches = spec_pitches)

@main.route('/category/<category>/new_pitch', methods = ['GET', 'POST'])
@login_required
def new_pitch(category):
    form = PitchForm()
    categ = category

    if form.validate_on_submit():
        pitch = form.pitch.data

        new_pitches = Pitch(category_pitch = categ, pitch_body = pitch)
        new_pitches.save_pitch()

        return redirect(url_for('main.show_pitches', category = categ))

    return render_template('new_pitch.html', form = form)
