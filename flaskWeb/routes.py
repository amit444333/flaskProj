from flask import render_template, url_for, flash, redirect, request
from flaskWeb import app, db, bcrypt
from flaskWeb.forms import RegistrationForm, LoginForm
from flaskWeb.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        "author": 'Amit Ben Amara',
        "title": 'First post',
        "content": 'OneDrive sucks dick',
        "date_posted": '20.07.2024' 
    },
    {
        "author": 'Amit Ben Amara',
        "title": 'Second post',
        "content": 'OneDrive sucks sooooo much dick',
        "date_posted": '21.07.2024' 
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hased_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hased_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Hate Account Created For {form.username.data}! You are able to log in and start hating', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Hatein Unsuccessful. Please check your Hate info', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')