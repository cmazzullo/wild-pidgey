#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12387                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

print ("Starting up s(" + str(s) + ") host(" + str(host) + ") port(" + str(port) + ")")

#for player1
s.listen(5)                 # Now wait for client connection.
while True:
   conn1, addr1 = s.accept()     # Establish connection with client.
   if conn1 and addr1:
       print 'Got connection from ', addr1
       conn1.send('Thank you for connecting')
       break


#for player2
s.listen(5)                 # Now wait for client connection.
while True:
   conn2, addr2 = s.accept()     # Establish connection with client.
   if conn2 and addr2:
       print 'Got connection from ', addr2
       conn2.send('Thank you for connecting')
       break


while True:
    print "Asking client for name..."
    name1 = conn1.recv(1024)
    name2 = conn2.recv(1024)
    if name1 and name2:
        conn1.send("Nice to meet you " + name1)
        conn2.send("Nice to meet you " + name2)
        break


while True:
   closeInput = raw_input("Type close to end all connections:  ")
   if closeInput == "close":
      print "about to close..."
      conn1.close()                  # Close the connection  
      conn2.close()
      print ("connection closed for " + str(addr1) + " and " + str(addr2))
      break
