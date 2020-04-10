from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        "author": "James Madison",
        "title": "US Constitution",
        "content": "The Articles of Confederation must be replaced.",
        "date_posted": "January 3, 2020"
    },
    {
        "author": "Troy McClure",
        "title": "Where are they going?",
        "content": "They are gone and nobody knows where.",
        "date_posted": "January 6, 2020"
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
