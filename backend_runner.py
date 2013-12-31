"""Master runner for the game in text mode.

This stocks the monster, attack and item databases and runs the game.
All of this is unimplemented."""

import monster

# the master list of all monsters
monsterlist = [	
#format: monster(self, name, types, vitality, speed, phys_strength, spirit_strength,
#                int_strength, phys_endur, spirit_endur, int_endur
	monster.Monster('pidgey', ['air', 'normal'], 90, 100, 20, 20, 30, 40, 40, 50)
]

for mon in monsterlist:
    print mon.str()

