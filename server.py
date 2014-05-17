import socket

def poll():
    HOST = ''
    PORT = 65000
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    (conn1, addr) = s.accept()
    conn1.sendall(b'client 1 connected')
    conn1.recv(1024)

    (conn2, addr) = s.accept()
    conn2.sendall(b'client 2 connected')
    conn2.recv(1024)
    return (conn1, conn2)

# takes connected socket
# gets player name from client
def get_player_name(conn):
    conn.sendall(b'get_name')
    return conn.recv(1024)

# takes connected socket
# prompts for action choice
# returns the name of the choice
def choose_action(player):
    player['conn'].sendall(b'choose_action')
    return player['conn'].recv(1024)

# prompts for attack choice
# returns attack chosen
def choose_attack(player):
    attack_list = b'choose_attack'
    c = 1
    for a in player['lead']['attacks']:
        attack_list = attack_list + str(c) + '. ' + a.name + '\n'
        c += 1
    player['conn'].sendall(attack_list)
    n =  player['conn'].recv(1024)
    return player.lead.attacks[int(n) - 1]

# prompts for lead choice
# returns lead
def choose_lead(player):
    lead_list = 'choose_lead'
    c = 1
    for m in player['monsters']:
        lead_list = lead_list + str(c) + '. ' + m['name'] + '\n'
        c += 1
    player['conn'].sendall(lead_list.encode('ascii'))
    n = player['conn'].recv(1024).decode('ascii')
    return player['monsters'][int(n) - 1]

# prompts for state choice
# returns state
def choose_state(player):
    player['conn'].sendall(b'choose_state')
    states = ('solid', 'liquid', 'gas', 'plasma')
    n = player['conn'].recv(1024).decode('ascii')
    return states[int(n) - 1]

def send_state(state, p1, p2):
    p1['conn'].sendall(('state' + state).encode('ascii'))
    p1['conn'].recv(1024)
    p2['conn'].sendall(('state' + state).encode('ascii'))
    p2['conn'].recv(1024)

def send_loss (player):
    player['conn'].sendall(b'loss')
    player['conn'].recv(1024)

def send_win (player):
    player['conn'].sendall(b'win')
    player['conn'].recv(1024)
