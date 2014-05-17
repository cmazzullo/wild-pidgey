import database
import server

def run_game():
    (conn1, conn2) = server.poll()
    name1 = server.get_player_name(conn1)
    name2 = server.get_player_name(conn2)
    
    p1 = database.get_player(name1.decode('ascii'))
    print ('gotplayername %s' % name1)
    p1['conn'] = conn1
    p2 = database.get_player(name2.decode('ascii'))
    p2['conn'] = conn2
    
    on_player = p1
    off_player = p2

    on_player['lead'] = server.choose_lead(on_player)
    off_player['lead'] = server.choose_lead(off_player)
    
    while not(has_lost(p1) or has_lost(p2)):
        server.send_state(get_state(p1, p2), p1, p2)
        if on_player['lead']['hp'] > 0:
            action = server.choose_action(on_player)
        else:
            action = 'switch'
        if action == 'attack':
            attack = server.choose_attack(on_player)
            attacker = on_player['lead']
            defender = off_player['lead']
            defender['hp'] -= (attacker['phys_strength'] / 10.0) * attack.damage
            if defender.hp <= 0:
                off_player['monsters'].remove (defender)
        elif action == 'switch':
            on_player['lead'] = server.choose_lead(on_player)
        elif action == 'state':
            on_player.lead.state = server.choose_state(on_player)
        on_player, off_player = off_player, on_player

    if has_lost(p1):
        server.send_loss (p1)
        server.send_win (p2)
    else:
        server.send_win (p1)
        server.send_loss (p2)
      
    p1.close()
    p2.close()

def has_lost (player):
    for m in player['monsters']:
        if m['hp'] > 0:
            return False
    return True

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
                    p1['name'], p1['lead']['name'], p1['lead']['hp'],
                    p1['lead']['current_state'], p2['name'], p2['lead']['name'],
                    p2['lead']['hp'], p2['lead']['current_state'])

run_game()
