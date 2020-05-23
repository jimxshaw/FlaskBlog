from flask import render_template, url_for, flash, redirect
from src import app
from src.forms import RegistrationForm, LoginForm
from src.models import User, Post


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


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You are logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login failed. Please check username and password.", "danger")
    return render_template("login.html", title="Login", form=form)
