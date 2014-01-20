class Attack:
	def __init__(self, name, base_damage, attack_type, attack_attribute, \
                 stat_mod = None, status_effect = None):
       	 self.base_damage = base_damage
         self.attack_type = attack_type
         self.attack_attribute = attack_attribute
         self.stat_mod = stat_mod
         self.status_effect = status_effect
         self.name = name
