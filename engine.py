import database
import server as s

def run_game():
    (conn1, conn2) = s.poll()
    name1 = s.get_player_name(conn1)
    name2 = s.get_player_name(conn2)
    
    p1 = database.get_player(name1)
    p1['conn'] = conn1
    p2 = database.get_player(name2)
    p2['conn'] = conn2
    print(p1)
    on = p1
    off = p2

    on['lead'] = s.choose_lead(on)
    off['lead'] = s.choose_lead(off)
    
    while not((p1loss = has_lost(p1))
               or has_lost(p2)):
        s.send_state(get_state(p1, p2), p1, p2)
        if on['lead'].hp > 0:
            action = s.choose_action(on)
        else:
            action = 'switch'
        if action == 'attack':
            attack = s.choose_attack(on)
            defender = off['lead']
            defender.hp -= (on['lead'].stats['phys_strength']
                                     / 10.0) * attack['damage']
            if defender.hp <= 0:
                off['monsters'].remove (defender)
        elif action == 'switch':
            on['lead'] = s.choose_lead(on)
        elif action == 'state':
            on['lead'].current_state = s.choose_state(on)
        on, off = off, on

    if p1loss:
        s.send_loss (p1)
        s.send_win (p2)
    else:
        s.send_win (p1)
        s.send_loss (p2)
      
    p1['conn'].close()
    p2['conn'].close()

def has_lost (player):
    for m in player['monsters']:
        if m.hp > 0:
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
                    p1['name'], p1['lead'].stats['name'], p1['lead'].hp,
                    p1['lead'].current_state, p2['name'], p2['lead'].stats['name'],
                    p2['lead'].hp, p2['lead'].current_state)

run_game()
