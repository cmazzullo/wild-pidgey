#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12393                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c1, addr1 = s.accept()     # Establish connection with client.
   s.listen(5)              # Wait for a second client
   c2, addr2 = s.accept()
   if c1 and addr1:
       print '(Client 1: Got connection from ', addr1
       c.send('Thank you for connecting')
   if c2 and addr2:
       print '(Client 2: Got connection from ', addr2
       c2.send('Thank you for connecting as well')

while True:
    print "Asking client for name..."
    player1_name = c1.recv(1024)
    player2_name = c2.recv(1024)
    if player1_name:
        c1.send("Nice to meet you " + player1_name)
    if player2_name:
        c2.send("Nice to meet you " + player2_name)
        break

print "about to close..."
c.close()                  # Close the connection
print ("connection closed for " + str(addr))
