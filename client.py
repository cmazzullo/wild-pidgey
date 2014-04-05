# Python prompted client
# this client connects to a server, which prompts it for a response
# the client then asks the user for input, which it relays to the 
# server. 

# I want to abstract this into a general client-server interface
# for the game States of Matter.

# This will be between the client logic and the server engine, swapping
# game state and player actions via strings.

import socket
import fileinput # needed for interactive user input

HOST = socket.gethostname() # runs on the local host
PORT = 65000 # high ports are less likely to be reserved
name = ''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print(s.recv(1024))
s.sendall('confirm')

def process(data):
    if data == 'get_name':
        return get_name()
    elif data == 'choose_action':
        return choose_action()
    elif data[:13] == 'choose_attack':
        return choose_attack(data[13:])
    elif data[:11] == 'choose_lead':
        return choose_lead(data[11:])
    elif data == 'choose_state':
        return choose_state()
    elif data[:5] == 'state':
        return recieve_state(data[5:])
    
def get_name():
    print "Please enter your Player Name: "
    name = raw_input('--> ')
    return name

def choose_action():
    print str.format("{}'s turn:",name)
    while True:
        s = raw_input('Do you want to:\n1. Attack\n2. Switch\n3.'
                      ' Change State\n--> ')
        if s == '1':
            return 'attack'
        elif s == '2':
            return 'switch'
        elif s == '3':
            return 'state'
        else:
            print "Please enter a valid option."

def choose_attack(attack_string):
    print 'Which attack:\n'
    print attack_string
    # this input needs error checking later
    attack = raw_input('--> ')
    return attack

def choose_lead(lead_string):
    print 'Which lead:\n'
    print lead_string
    lead = raw_input('--> ')
    return lead

def choose_state():
    print 'Which state:\n1. Solid\n2. Liquid\n3. Gas\n4. Plasma\n'
    state = raw_input('--> ')
    return state

def recieve_state(state):
    print state
    return 'confirm'

# this is the main loop of the client
reply = ''
while reply != 'quit':
    data = s.recv(1024)
    reply = process(data)
    s.sendall(reply)
