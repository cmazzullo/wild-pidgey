"""Master runner for the game in text mode.

This stocks the monster, attack and item databases and runs the game.
All of this is unimplemented."""

import Monster
import Attack


# the master list of all monsters
monster_list = [	
#format: monster(self, name, types, vitality, speed, phys_strength, spirit_strength,
#                int_strength, phys_endur, spirit_endur, int_endur
    Monster.Monster('Pidgey', ['air', 'normal'], 90, 100, 20, 20, 30, 40, 40, 50)
]


attack_list = [
    Attack.Attack('Tackle', 'normal', '35')
]

for a in attack_list:
    print a.str()

