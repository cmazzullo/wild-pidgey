#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12388                # Reserve a port for your service.
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
<<<<<<< HEAD
   conn2, addr2 = s.accept()     # Establish connection with client.
   if conn2 and addr2:
       print 'Got connection from ', addr2
       conn2.send('Thank you for connecting')
       break
=======
   c, addr = s.accept()     # Establish connection with client.
   s.listen(5)              # Wait for a second client
   c2, addr2 = s.accept()
   if c and addr:
       print '(Client 1: Got connection from ', addr
       c.send('Thank you for connecting')
   if c2 and addr2:
       print '(Client 2: Got connection from ', addr2
       c2.send('Thank you for connecting as well')
>>>>>>> ea069f00179b49fb9f713d6967c2578eaaedb755


while True:
    print "Asking client for name..."
    name1 = conn1.recv(1024)
    name2 = conn2.recv(1024)
    if name and name2:
        conn1.send("Nice to meet you " + name1)
        conn2.send("Nice to meet you " + name2)
        break


<<<<<<< HEAD

while True:
   closeInput = raw_input("Type close to end all connections:  ")
   if closeInput == "close":
      print "about to close..."
      conn1.close()                  # Close the connection  
      conn2.close()
      print ("connection closed for " + str(addr1) + " and " + str(addr2))
      break

=======
print "about to close..."
c.close()                  # Close the connection
print ("connection closed for " + str(addr))
>>>>>>> ea069f00179b49fb9f713d6967c2578eaaedb755
