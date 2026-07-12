
from datetime import date
from shuttle_stats.models import Match
from shuttle_stats.stats import win_rates
from shuttle_stats.app import app

def main() -> None:
    # test data
    matches = [
        Match("Eric", "Alex", 21, 15, date(2026, 7, 1)),
        Match("Eric", "Alex", 18, 21, date(2026, 7, 5)),
        Match("Eric", "Sam", 21, 10, date(2026, 7, 8)),
        Match("Eric", "Sam", 10, 21, date(2026, 7, 8))
    ]

    print("Win rates:" + str(win_rates(matches)))




if __name__ == "__main__":
    app.run(debug=True)
