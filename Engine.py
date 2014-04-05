import Database
import server

# PUBLIC METHODS:

# starts the game between the two players
# returns the name of the winner
def run_game():
    (conn1, conn2) = server.poll()
    name1 = server.get_player_name(conn1)
    name2 = server.get_player_name(conn2)
    p1 = (Database.get_player(name1), conn1) # store the players as  
    p2 = (Database.get_player(name2), conn2) # tuples containing all
    on_player = p1                           # their data and their
    off_player = p2                          # connected socket

    while not game_over():
        server.send_state(get_state(p1[0], p2[0]), p1, p2)
        action = server.choose_action(on_player)
        if action == 'attack':
            attack = server.choose_attack(on_player)
            attacker = on_player[0].lead
            defender = off_player[0].lead
            #ATTACK LOGIC GOES HERE!
            defender.hp -= (attacker.phys_strength / 10) * attack.damage
        elif action == 'switch':
            on_player[0].lead = server.choose_lead(on_player)
        elif action == 'state':
            on_player[0].lead.state = server.choose_state(on_player)
        on_player, off_player = off_player, on_player
    return _get_winner()
        
# returns the winning player's name after a game is over
def get_winner():
    pass

# returns true is game is over, otherwise false
def game_over():
    pass

def get_state(p1, p2):
    return str.format('============================================\n'             
                   'Player 1: {}\n'                                             
                   'Lead: {}\n'                                                 
                   'HP: {}\n'                                                   
                   'State: {}\n'
                   '--------------------------------------------\n'                
                   'Player 2: {}\n'                                             
                   'Lead: {}\n'                                                 
                   'HP: {}\n'                                                   
                   'State: {}\n'
                   '============================================\n',               
                   p1.name, p1.lead.name, p1.lead.hp, p1.lead.state,
                   p2.name, p2.lead.name, p2.lead.hp, p2.lead.state)


run_game()
