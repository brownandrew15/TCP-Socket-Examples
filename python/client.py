import socket

#Settings for the Client
ipAddress = "192.168.0.3"
port = 43125
maxReceive = 4096

#create a socket
connection = socket.socket()

# connect to the server with the given ip address and port
connection.connect((ipAddress, port))

#Enter the message to send
toSend = input("Enter the message to send: ")

#While "END" is not the message to send
while toSend != "END":

    #Send the data to the server
    connection.send(bytes(toSend, "utf-8"))

    #tell the user that the program is waiting for a response
    print("Waiting for response")

    #print the response from the server
    print("Received: " + str(connection.recv(maxReceive)))

    #Enter the next message to send
    toSend = input("Enter the message to send: ")

# close the connection
connection.close()
