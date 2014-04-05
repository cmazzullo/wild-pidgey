import socket

# these contain all important information about the connected players
# playerN = (name, connection, number) where number is 1 or 2

# waits for a player to connect
# returns a nested tuple containing both client sockets
# in the form (conn1, conn2)
# this is unpacked in the Engine script
def poll():
    HOST = ''
    PORT = 65000
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    (conn1, addr) = s.accept()
    (conn2, addr) = s.accept()

    conn1.sendall('client 1 connected')
    conn1.recv(1024)
    conn2.sendall('client 2 connected')
    conn2.recv(1024)
    return (conn1, conn2)

# takes connected socket
# gets player name from client
def get_player_name(conn):
    conn.sendall('get_name')
    return conn.recv(1024)

# takes connected socket
# prompts for action choice
# returns the name of the choice
def choose_action((player, conn)):
    conn.sendall('choose_action')
    return conn.recv(1024)

# prompts for attack choice
# returns attack chosen
def choose_attack((player, conn)):
    attack_list = 'choose_attack'
    c = 1
    for a in player.lead.attacks:
        attack_list = attack_list + str(c) + '. ' + a.name + '\n'
        c += 1
    conn.sendall(attack_list)
    n =  conn.recv(1024)
    return player.lead.attacks[int(n) - 1]

# prompts for lead choice
# returns lead
def choose_lead((player, conn)):
    lead_list = 'choose_lead'
    c = 1
    for m in player.monsters:
        lead_list = lead_list + str(c) + '. ' + m.name + '\n'
        c += 1
    conn.sendall(lead_list)
    n = conn.recv(1024)
    return player.monsters[int(n) - 1]

# prompts for state choice
# returns state
def choose_state((player, conn)):
    conn.sendall('choose_state')
    states = ('solid', 'liquid', 'gas', 'plasma')
    n = conn.recv(1024)
    return states[int(n) - 1]

def send_state(state, (p1, conn1), (p2, conn2)):
    conn1.sendall('state' + state)
    conn1.recv(1024)
    conn2.sendall('state' + state)
    conn2.recv(1024)
