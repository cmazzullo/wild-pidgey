from attack import attack
from monster import Monster

class Player():

    def __init__(self, name):
        self.name = name
        self.monsters = []
        self.lead = None
        self.current_attack = None

    def set_monsters(self, monsters):
        if len(monsters) > 6 or len(monsters) <= 0:
            return False
        self.monsters = []
        for m in monsters:
            self.monsters.append(m)
        self.lead = self.monsters[0]
        return True

    def make_move(self, move, choice):
        if move == "switch":
            self.lead = choice
            self.current_attack = None
        elif move == "attack":
            self.current_attack = choice

    def has_lost(self):
        for m in self.monsters:
            if not(m.hp <= 0):
                return False
        return True
