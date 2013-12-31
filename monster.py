class Monster:
	"""A framework for the monsters in States of Matter"""

	# creates a monster with certain stats
	# eventually, stats should be stored in a database rather than passed by parameter
	# would look like: def __init__(self, KEY) where key is the name of the monster
	def __init__(self, v, spd, phys_str, spr_str, int_str, phys_end, spr_end, int_end):
		self.vitality =		v 
		self.speed =		spd 

		self.phys_strength =	phys_str 
		self.spirit_strength =	spr_str 
		self.int_strength =	int_str 

		self.phys_endur =	phys_end 
		self.spirit_endur = 	spr_end
		self.int_endur = 	int_end

	# returns total outgoing damage for a given attack
	def attack(self, base_dmg):
		return (phys_strength - phys_endur)
