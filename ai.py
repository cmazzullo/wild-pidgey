from player import Player
from attack import attack
from monster import monster

class ai():
    
    def __init__(self, ai_player):
        self.name = 'Computer'
        self.monsters = ai_player.monsters
        self.lead = ai_player.lead
        self.current_attack = lead.moveset[0]

