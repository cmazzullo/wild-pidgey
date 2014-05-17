class Attack:
    def __init__(self, name, damage, types, stat_mods):
        self.name = name
        self.damage = damage
        self.types = types
        self.stat_mods = stat_mods

attacks = [
    {'name': 'att1', 'damage': 1, 'type': 'normal', 'smods': None},
    {'name': 'att1', 'damage': 1, 'type': 'normal', 'smods': None},
    {'name': 'att1', 'damage': 1, 'type': 'normal', 'smods': None},
    {'name': 'att1', 'damage': 1, 'type': 'normal', 'smods': None}]


def get_attack(name):
    for a in attacks:
        if a['name'] == name:
            return a

#name, types, attack_names, vitality, speed, 
 #                phys_strength, spirit_strength, int_strength, phys_endur, 
  #               spirit_endur, int_endur

    
# Create monsters, the master list of monsters
monsters = []
f = open('Data.txt')
for line in f.readlines():
    l = line.split(';')
    monsters.append({'name': l[0],
                    'types': l[1].split(','),
                    'attack_names': l[2].split(','),
                    'vitality': int(l[3]), 
                    'speed': int(l[4]),
                    'phys_strength': int(l[5]),
                    'spirit_strength': int(l[6]),
                    'int_strength': int(l[7]),
                    'phys_endur': int(l[8]),
                    'spirit_endur': int(l[9]),
                    'int_endur': int(l[10]),
                    'hp': int(l[3]),
                    'current_state': 'solid'})

players = [
    {'name': 'p1', 'monsters':
    [monsters[0], monsters[1], monsters[3], monsters[2]]},
    {'name': 'p2', 'monsters':
    [monsters[0], monsters[1], monsters[2], monsters[3]]}]

# returns a player with the name from the database
def get_player(name):
    for p in players:
        if p['name'] == name:
            return p
