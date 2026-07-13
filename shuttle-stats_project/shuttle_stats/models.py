from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Match:
    player1: str
    player2: str
    player1_score: int
    player2_score: int
    date_played: datetime = field(default_factory=datetime.now)

    @property
    def winner(self) -> str:
        return self.player1 if self.player1_score > self.player2_score else self.player2
    
@dataclass
class Player:
    name: str