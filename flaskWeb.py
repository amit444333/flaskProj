from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '03b5f57049b9881b93cd9ef9b6df7bb0'

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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Hate Account Created For {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@hate.com' and form.password.data == 'hate':
            flash('You have been hated in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Hatein Unsuccessful. Please check your Hate info', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)