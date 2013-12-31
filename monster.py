class Monster:
    """A framework for the monsters in States of Matter"""

    # creates a monster with certain stats
    # eventually, stats should be stored in a database rather than passed by parameter
    # would look like: def __init__(self, KEY) where key is the name of the monster
    def __init__(self, name, types, vitality, speed, phys_strength, spirit_strength, 
               	 int_strength, phys_endur, spirit_endur, int_endur):
	self.name		= name
	self.types		= types

        self.vitality 		= vitality
        self.speed 		= speed 
        self.phys_strength 	= phys_strength 
        self.spirit_strength	= spirit_strength
        self.int_strength 	= int_strength
        self.phys_endur 	= phys_endur
        self.spirit_endur 	= spirit_endur
        self.int_endur 		= int_endur

    # returns total outgoing damage for a given attack - not implemented
    def send_attack(self, base_dmg, attack_type, stat_mod, condition):
        return (phys_strength - phys_endur)
    
    # processes incoming attacks - not implemented
    def recieve_attack(self, base_dmg, attack_type, stat_mod, condition):
        pass

    def str(self):
        print 'Name:', self.name, 'Types:', self.types, 'Vitality:', self.vitality,
	'Speed:', self.speed, 'Physical strength:', self.phys_strength,
	'Spirit Strength:', self.spirit_strength, 'Intellectual Strength:',
	self.int_strength, 'Pysical endurance:', self.phys_endur, 
	'Spiritual Endurance:', self.spirit_endur, 'Intellectual Endurance:',
	self.int_endur

