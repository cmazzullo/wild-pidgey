import Database
import Fakeserver


# PUBLIC METHODS:

# starts the game between the two players
# returns the name of the winner
def start_game(name1, name2):
    on_player = Database.get_player(name1)
    off_player = Database.get_player(name2)
    while not game_over():
        print get_state(on_player, off_player)
        do_turn(on_player, off_player)
        on_player, off_player = off_player, on_player
    return _get_winner()
        
# prompts for an action choice from the player
# returns the action choice
def choose_action(player):
    return Fakeserver.choose_action(player)
    
# prompts for a lead choice from the player
# returns the lead choice
def choose_lead(player):
    return Fakeserver.choose_lead(player, player.monsters)

# prompts for an attack choice from the player
# returns the attack choice
def choose_attack(player):
    return Fakeserver.choose_attack(player, player.lead.attacks)

# prompts for a state choice from the player
# returns the state choice
def choose_state(player):
    return Fakeserver.choose_state(player)

# executes one turn for the on_player
def do_turn(on_player, off_player):
    action = choose_action(on_player)
    if action == 'attack':
        attack = choose_attack(on_player)
        attacker = on_player.lead
        defender = off_player.lead
        #ATTACK LOGIC GOES HERE!
        defender.hp -= (attacker.phys_strength / 10) * attack.damage
    elif action == 'switch':
        on_player.lead = choose_lead(on_player)
    elif action == 'state':
        on_player.lead.state = choose_state(on_player)

# returns the winning player's name after a game is over
def get_winner():
    pass

# returns true is game is over, otherwise false
def game_over():
    pass

def get_state(p1, p2):
    return str.format('Player1: {}\nLead: {}\nHP: {}\nState: {}\n\n'
                      'Player2: {}\n' 'Lead: {}\nHP: {}\nState: {}\n', p1.name, 
                      p1.lead.name, p1.lead.hp, p1.lead.state, p2.name, 
                      p2.lead.name, p2.lead.hp, p2.lead.state)
