# Python prompted client

# This needs to be able to retrieve and process messages from a server
# and not crash on errors

import socket
import fileinput # needed for interactive user input

global s
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect ():
    HOST = socket.gethostname() # runs on the local host
    PORT = 65000 # high ports are less likely to be reserved
    name = ''
    s.connect((socket.gethostname(), PORT))
    print(s.recv(1024))
    s.sendall(b'confirm')

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
    elif data == 'loss':
        print ("you lose")
        return 'quit'
    elif data == 'win':
        print ("you win")
        return 'quit'
    else:
        return "error"
    
def get_name():
    print ("Please enter your Player Name: ")
    name = input('--> ')
    return name

def choose_action():
    print (str.format("Your turn:"))
    while True:
        response = input('Do you want to:\n1. Attack\n2. Switch\n3.'
                      ' Change State\n--> ')
        if response == '1':
            return 'attack'
        elif response == '2':
            return 'switch'
        elif response == '3':
            return 'state'
        else:
            print ("Please enter a valid option.")

def choose_attack(attack_string):
    print ('Which attack:\n')
    print (attack_string)
    attack = input('--> ')
    return attack

def choose_lead(lead_string):
    print ('Which lead:\n')
    print (lead_string)
    lead = input('--> ')
    return lead

def choose_state():
    print ('Which state:\n1. Solid\n2. Liquid\n3. Gas\n4. Plasma\n')
    state = input('--> ')
    return state

def recieve_state(state):
    print (state)
    return 'confirm'

def listen():
    # this is the main loop of the client
    reply = ''
    while reply != 'quit':
        data = s.recv(1024).decode('ascii')
        reply = process(data)
        s.sendall(reply.encode('ascii'))
    s.close()
    
connect()
listen()
