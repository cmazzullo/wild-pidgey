import socket

def message(conn, message):
    conn.sendall(message.encode('ascii'))
    return conn.recv(1024).decode('ascii')
    
def poll():
    HOST = ''
    PORT = 65000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    (conn1, addr) = s.accept()
    message(conn1, 'Client 1 connected')
    (conn2, addr) = s.accept()
    message(conn2, 'client 2 connected')
    return (conn1, conn2)

def get_player_name(conn):
    return message(conn, 'get_name')

def choose_action(player):
    return message(player['conn'], 'choose_action')

# prompts for attack choice
# returns attack chosen
def choose_attack(player):
    attack_list = 'choose_attack'
    c = 1
    for a in player['lead'].stats['attacks']:
        attack_list = attack_list + str(c) + '. ' + a['name'] + '\n'
        c += 1
    n = message(player['conn'], attack_list)
    return player['lead'].stats['attacks'][int(n) - 1]

# prompts for lead choice
# returns lead
def choose_lead(player):
    lead_list = 'choose_lead'
    c = 1
    for m in player['monsters']:
        lead_list = lead_list + str(c) + '. ' + m.stats['name'] + '\n'
        c += 1
    n = message(player['conn'], lead_list)
    return player['monsters'][int(n) - 1]

# prompts for state choice
# returns state
def choose_state(player):
    n = message(player['conn'], 'choose_state')
    states = ('solid', 'liquid', 'gas', 'plasma')
    return states[int(n) - 1]

def send_state(state, p1, p2):
    message(p1['conn'], 'state' + state)
    message(p2['conn'], 'state' + state)

def send_loss (player):
    message(player['conn'], 'loss')

def send_win (player):
    message(player['conn'], 'win')
