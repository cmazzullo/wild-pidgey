"""Master runner for the game in text mode.

This stocks the monster, attack and item databases and runs the game.
All of this is unimplemented."""

import monster
import player
import attack

# the master list of attacks
tackle = attack.attack(35, 'normal', 'physical')
tail_whip = attack.attack(0, 'normal', 'physical', 'phys_endur')

# the master list of all monsters
monster_list = [	
# format: monster(self, name, types, elements, moveset, vitality, speed, 
# phys_strength, spirit_strength, int_strength, phys_endur, spirit_endur,
# int_endur
    monster.Monster('Pidgey', ['air', 'normal'], 'plasma', [tackle, tail_whip],
                    90, 100, 20, 20, 30, 40, 40, 50)
]

# There are always two players:
player1 = player.Player('Ed')
player2 = player.Player('Gloria')

# The state needs to be reported after every turn
def print_state():
    print 'Player 1:\t', player1.name
    print '\tLead:\t', player1.lead

while(not player1.has_lost() and not player2.has_lost()):
    print_state()
    # first, player 1 takes a turn. It can either switch a monster out or 
    # choose an attack to perform.
    player2.lead.recieve_attack(player1.current_attack, player1.lead)
    
    if(player1.has_lost() or player2.has_lost()):
        break

    # here, player 2 chooses their move. then the attack is processed. 
    player1.lead.recieve_attack(player2.current_attack, player2.lead)


print 'Game over!'
if(player1.has_lost()):
    print player2.name + ' wins!'
else:
    print player1.name + ' wins!'
