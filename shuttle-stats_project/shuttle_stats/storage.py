import json
from dataclasses import asdict
from datetime import datetime
from pathlib import Path
from shuttle_stats.models import Match, Player

DATA_FILE = Path("data.json")

def save_data(matches: list[Match], players: list[Player]) -> None:
    data = {
        "matches": [asdict(match) for match in matches],
        "players": [asdict(player) for player in players],
    }
    for match in data["matches"]:
        match["date_played"] = match["date_played"].isoformat()
    
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def load_data() -> tuple[list[Match], list[Player]]:
    if not DATA_FILE.exists():
        return [], []

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    matches = []
    for match in data["matches"]:
        match["date_played"] = datetime.fromisoformat(match["date_played"])
        matches.append(Match(**match))

    players = [Player(**player) for player in data["players"]]
    return matches, players