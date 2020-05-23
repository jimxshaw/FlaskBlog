from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "7444f4c651c0b91684124cbfe1cb144b"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///flaskblog.db"
db = SQLAlchemy(app)

from src import routes