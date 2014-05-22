class Monster:
    def __init__(self, stats):
        self.stats = stats
        self.hp = stats['vitality']
        self.current_state = 'solid'

attacks = {
    'att1':    {'name': 'tackle', 'damage': 1, 'type': 'normal', 'smods': None},
    'att2':    {'name': 'slash', 'damage': 2, 'type': 'normal', 'smods': None},
    'att3':    {'name': 'take down', 'damage': 3, 'type': 'normal', 'smods': None},
    'att4':    {'name': 'headbutt', 'damage': 4, 'type': 'normal', 'smods': None}}

# Create monsters, the master list of monsters
monsters = []
f = open('Data.txt')
for line in f.readlines():
    l = line.split(';')
    namearray = l[2].split(',')
    attackarray = []
    for a in namearray:
        attackarray.append(attacks[a])
    monsters.append({'name': l[0],
                    'types': l[1].split(','),
                    'attacks': attackarray,
                    'vitality': int(l[3]), 
                    'speed': int(l[4]),
                    'phys_strength': int(l[5]),
                    'spirit_strength': int(l[6]),
                    'int_strength': int(l[7]),
                    'phys_endur': int(l[8]),
                    'spirit_endur': int(l[9]),
                    'int_endur': int(l[10])})

players = [
    {'name': 'p1', 'monsters':
    [Monster(monsters[0]), Monster(monsters[1]), Monster(monsters[3]), Monster(monsters[2])]},
    {'name': 'p2', 'monsters':
    [Monster(monsters[0]), Monster(monsters[1]), Monster(monsters[3]), Monster(monsters[2])]}]

def get_player(name):
    for p in players:
        if p['name'] == name:
            return p
