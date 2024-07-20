from flask import Flask, render_template, url_for

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)