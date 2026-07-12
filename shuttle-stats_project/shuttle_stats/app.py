from flask import Flask, render_template, request, redirect
from datetime import date
from shuttle_stats.models import Match
from shuttle_stats.stats import win_rates

app = Flask(__name__)

matches: list[Match] = []

@app.route("/")
def home():
    rates = win_rates(matches) if matches else {}
    return render_template("index.html", matches=matches, rates=rates)

@app.route("/add", methods=["GET", "POST"])
def add_match():
    if request.method == "POST":
        player1 = request.form["player1"]
        player2 = request.form["player2"]
        player1_score = int(request.form["player1_score"])
        player2_score = int(request.form["player2_score"])
        match = Match(player1, player2, player1_score, player2_score, date.today())
        matches.append(match)
        return redirect("/")
    return render_template("add_match.html")