from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Match:
    player1: str
    player2: str
    player1_score: int
    player2_score: int
    date_played: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        if self.player1 == self.player2:
            raise ValueError("Players must be different.")
        if self.player1_score < 0 or self.player2_score < 0:
            raise ValueError("Scores must be non-negative.")
        if self.player1_score == self.player2_score:
            raise ValueError("There must be a winner (no ties allowed).")

    @property
    def winner(self) -> str:
        return self.player1 if self.player1_score > self.player2_score else self.player2
    
@dataclass
class Player:
    name: str