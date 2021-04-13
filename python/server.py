import socket

#Settings for the server
port = 43125
maxReceive = 4096

#Create a socket that the server will use
socket = socket.socket()

#Bind the port to the socket
socket.bind(('', port))

#Start the server listening for connections
socket.listen()

#Tell the user that the server has started
print("Server started - waiting for connection")

# accept a connection (returns a tuple)
c = socket.accept()

#Split the tuple object to its components
connection = c[0]
address = str(c[1])

#tell the user the ip address of the client that has connected
print("Connection established with " + address)

#recieve a message
message = connection.recv(maxReceive).decode("utf-8").strip()

#While the server doesn't receive "END"
while message != "END":

    #display the message that the server received
    print("Server recieved: " + message)

    #Send a response message
    connection.send(bytes("Server received: " + message, 'utf-8'))

    #receive the next message
    message = connection.recv(maxReceive).decode("utf-8").strip()

# close the connection to the client
connection.close()
