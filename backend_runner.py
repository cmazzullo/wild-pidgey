"""Master runner for the game in text mode.

This stocks the monster, attack and item databases and runs the game."""

from attack import Attack
from monster import Monster
from player import Player

# the master list of attacks
tackle = Attack('Tackle', 35, 'normal', 'physical')
tail_whip = Attack('Tail Whip', 0, 'normal', 'physical', 'phys_endur')

# format: monster(self, name, types, elements, moveset, vitality, speed, 
# phys_strength, spirit_strength, int_strength, phys_endur, spirit_endur,
# int_endur
monster_list = [
Monster('Pidgey', ['air', 'normal'], 'plasma', [tackle, tail_whip],
                    90, 100, 200, 20, 30, 40, 40, 50),
Monster('Vulpix', 'fire', 'plasma', [tackle, tail_whip],
                    90, 100, 20, 20, 30, 40, 40, 50)
]

def make_monster(name):
    for m in monster_list:
        if m.name == name:
            return Monster(name, m.types, m.elements, m.moveset, m.vitality,
                           m.speed, m.phys_strength, m.spirit_strength,
                           m.int_strength, m.phys_endur, m.spirit_endur, 
                           m.int_endur)

# There are always two players:
player1 = Player('Ed')
player2 = Player('Gloria')

player1.set_monsters([make_monster('Vulpix'), make_monster('Pidgey')])
player2.set_monsters([make_monster('Vulpix')])

# The state needs to be reported after every turn
def print_state():
    print '========================================='
    print 'Player 1:\t', player1.name
    print '\tLead:\t', player1.lead.name
    print '\tHP:\t', player1.lead.hp
    print '-----------------------------------------'
    print 'Player 2:\t', player2.name
    print '\tLead:\t', player2.lead.name
    print '\tHP:\t', player2.lead.hp
    print '========================================='

# Performs the turn of the player passed as a parameter
def do_turn(p):
    while(True):
        _input = raw_input("Type 'a' to attack or 's' to switch.")

        # If the player wants to attack:
        if(_input == 'a'):
            c = 1
            for a in p.lead.moveset:
                print (str(c) + '. '+ a.name)
                c += 1

            while(True):
                _input = raw_input("Type the number of the attack you'd like " 
                "to use.")
                if(_input == '1'):
                    p.make_move('attack', p.lead.moveset[0])
                    break
                elif(_input == '2'):
                    p.make_move('attack', p.lead.moveset[1])
                    break
                elif(_input == '3'):
                    p.make_move('attack', p.lead.moveset[2])
                    break
                elif(_input == '4'):
                    p.make_move('attack', p.lead.moveset[3])
                    break

            print ''
            print '!!!Player 1 attacks with ', p.current_attack.name
            print ''
            break

        # If player1 wants to switch:
        elif(_input == 's'):
            c = 1
            for m in p.monsters:
                print (str(c) + '. ' + m.name)
                c += 1
            while(True):
                _input = raw_input("Type the number of the monster you'd like " 
                                   "to use.")
                if(_input == '1'):
                    p.make_move('switch', p.monsters[0])
                    break
                elif(_input == '2'):
                    p.make_move('switch', p.monsters[1])
                    break
                elif(_input == '3'):
                    p.make_move('switch', p.monsters[2])
                    break
                elif(_input == '4'):
                    p.make_move('switch', p.monsters[3])
                    break
                elif(_input == '5'):
                    p.make_move('switch', p.monsters[4])
                    break
                elif(_input == '6'):
                    p.make_move('switch', p.monsters[5])
                    break

            print ''
            print '!!!Player 2 switches to ', p.lead.name
            print ''
            break


# The main loop of the game, runs everything
while(not player1.has_lost() and not player2.has_lost()):
    print_state()
    print "------------Player 1's turn----------"
    do_turn(player1)
    player2.lead.recieve_attack(player1.current_attack, player1.lead)

    print_state()
    if(player1.has_lost() or player2.has_lost()):
        break

    print "------------Player 2's turn----------"
    do_turn(player2)
    player1.lead.recieve_attack(player2.current_attack, player2.lead)


print 'Game over!'
if(player1.has_lost()):
    print player2.name + ' wins!'
else:
    print player1.name + ' wins!'
