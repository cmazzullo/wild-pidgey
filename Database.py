class Attack:
    def __init__(self, name, damage, types, stat_mods):
        self.name = name
        self.damage = damage
        self.types = types
        self.stat_mods = stat_mods

attacks = [
Attack('att1', 1, 'normal', None),
Attack('att2', 2, 'normal', None),
Attack('att3', 3, 'normal', None),
Attack('att4', 4, 'normal', None)
]

def get_attack(name):
    for a in attacks:
        if a.name == name:
            return a

class Monster:
    def __init__(self, name, types, attack_names, vitality, speed, 
                 phys_strength, spirit_strength, int_strength, phys_endur, 
                 spirit_endur, int_endur):
        self.name = name
        self.types = types
        self.attack_names = attack_names
        self.attacks = []
        for a in attack_names:
            self.attacks.append(get_attack(a))
    
        #used to save base stats
        self.vitality = vitality
        self.speed = speed 
        self.phys_strength 	= phys_strength 
        self.spirit_strength	= spirit_strength
        self.int_strength = int_strength
        self.phys_endur	= phys_endur
        self.spirit_endur = spirit_endur
        self.int_endur = int_endur
    
        #used to save temporary stats per battle
        self.hp = vitality
        self.temp_speed = speed 
        self.temp_phys_strength	= phys_strength 
        self.temp_spirit_strength = spirit_strength
        self.temp_int_strength = int_strength
        self.temp_phys_endur = phys_endur
        self.temp_spirit_endur = spirit_endur
        self.temp_int_endur = int_endur
        self.state = 'solid'

    def __str__(self):
        s = str.format(
            """Name:                {}
Types:               {}
Attacks:             {}
Vitality:            {}
Speed:               {}
Physical Strength    {}
Spirit Strength      {}
Mental Strength      {}
Pysical Endurance    {}
Spirit Endurance     {}
Mental Endurance     {}\n""", self.name, self.types, self.attack_names,
               self.vitality, self.speed, self.phys_strength,
               self.spirit_strength, self.int_strength, self.phys_endur,
               self.spirit_endur, self.int_endur)
        return s
    
# Create monsters, the master list of monsters
monsters = []
f = open('Data.txt')
for line in f.readlines():
    l = line.split(';')
    monsters.append(Monster(l[0], l[1].split(','), l[2].split(','), int(l[3]), 
                    int(l[4]), int(l[5]), int(l[6]), int(l[7]), int(l[8]),
                    int(l[9]), int(l[10])))

def make_monster(name):
    for m in monsters:
        if m.name == name:
            return Monster(m.name, m.types, m.attack_names, m.vitality,
                           m.speed, m.phys_strength, m.spirit_strength, 
                           m.int_strength, m.phys_endur, m.spirit_endur,
                           m.int_endur)

class Player:
    def __init__(self, name, monster_names):
        self.name = name
        self.monsters = []
        for m in monster_names:
            self.monsters.append(make_monster(m))
        self.lead = self.monsters[0]

players = [
Player('p1', ['mon1', 'mon2', 'mon3', 'mon4']),
Player('p2', ['mon1', 'mon2', 'mon3', 'mon4'])
]

# Methods:

# returns a player with the name from the database
def get_player(name):
    for p in players:
        if p.name == name:
            return p
