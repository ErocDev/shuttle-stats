from flask import Flask, render_template, request, redirect
from datetime import date
from shuttle_stats.models import Match, Player
from shuttle_stats.stats import win_rates

app = Flask(__name__)

matches: list[Match] = []
players: list[Player] = []

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

        errors = []
        if player1 == player2:
            errors.append("Players must be different.")
        if player1_score < 0 or player2_score < 0:
            errors.append("Scores must be non-negative.")
        if player1_score == player2_score:
            errors.append("There must be a winner (no ties allowed).")
        
        if errors:
            return render_template("add_match.html", players=players, errors=errors)

        match = Match(player1, player2, player1_score, player2_score)
        matches.append(match)
        return redirect("/")
    return render_template("add_match.html", players=players)

@app.route("/players", methods=["GET", "POST"])
def manage_players():
    if request.method == "POST":
        name = request.form["name"].strip()
        if name and not any(p.name == name for p in players):
            players.append(Player(name))
        return redirect("/players")
    
    return render_template("players.html", players=players)