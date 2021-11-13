from cs50 import SQL
from flask import Flask, render_template, request

app = Flask(__name__)

db = SQL("sqlite:///cascades.db")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search")
def search():
    cascades = db.execute("SELECT * FROM cascades WHERE output= ?", request.args.get("q") )
    return render_template("search.html",  cascades = cascades)

