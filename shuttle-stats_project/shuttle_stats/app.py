from flask import Flask, render_template, request, redirect
from shuttle_stats.models import Match, Player
from shuttle_stats.stats import win_rates
from shuttle_stats.storage import save_data, load_data

app = Flask(__name__)

matches, players = load_data()

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
        
        try:
            match = Match(player1, player2, player1_score, player2_score)
        except ValueError as e:
            return render_template("add_match.html", players=players, errors=[str(e)])
        
        matches.append(match)
        save_data(matches, players)
        return redirect("/")    
    return render_template("add_match.html", players=players)

@app.route("/players", methods=["GET", "POST"])
def manage_players():
    if request.method == "POST":
        name = request.form["name"].strip()
        if name and not any(p.name == name for p in players):
            players.append(Player(name))
        save_data(matches, players)
        return redirect("/players")
    
    return render_template("players.html", players=players)

@app.route("/match/<match_id>")
def match_detail(match_id):
    match = next((m for m in matches if m.id == match_id), None)
    if match is None:
        return "Match not found", 404
    return render_template("match_detail.html", match=match)

@app.route("/match/<match_id>/delete", methods=["POST"])
def delete_match(match_id):
    global matches
    matches = [m for m in matches if m.id != match_id]
    save_data(matches, players)
    return redirect("/")

@app.route("/players/<player_id>/delete", methods=["POST"])
def delete_player(player_id):
    global players
    players = [p for p in players if p.id != player_id]
    save_data(matches, players)
    return redirect("/players")

