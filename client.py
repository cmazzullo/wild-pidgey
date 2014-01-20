#!/usr/bin/python           # This is client.py file

import socket               # Import socket module


def createClient(name):
    s = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    port = 12387                # Reserve a port for your service.

    s.connect((host, port))
    print s.recv(1024)
    print "Sending name..."
    s.send(name)
    print "Name sent."
    print s.recv(1024)

    s.close                     # Close the socket when done
    print ("connection closed for server " + str(s))

    """
    while True:
        closeInput = raw_input("Enter close if you want to close connection:  ")
        if closeInput == "close":
            s.close                     # Close the socket when done
            print ("connection closed for server " + str(s))
            break
    """
