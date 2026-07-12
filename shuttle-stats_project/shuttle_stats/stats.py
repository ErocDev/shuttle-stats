from collections import defaultdict
from shuttle_stats.models import Match

def win_rates(matches: list[Match]) -> dict[str, float]:
    # Calculate the win rates for each player based on a list of matches.

    # Args:
    #     matches (list[Match]): A list of Match objects.

    played: dict[str, int] = defaultdict(int)
    won: dict[str, int] = defaultdict(int)

    for match in matches:
        played[match.player1] += 1
        played[match.player2] += 1
        won[match.winner] += 1

    return {
        player: won[player] / played[player]
        for player in played
    }