from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "7444f4c651c0b91684124cbfe1cb144b"

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
    return render_template("about.html", title="About")


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Register", form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)
