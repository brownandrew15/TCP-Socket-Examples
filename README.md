# TCP Socket Examples

## About
The programs in this repository are basic Client and Server TCP socket programs.
They are as basic as they can be, comments are provided to explain what each section does.

All programs can be run as is but will need to be expanded to get the most out of them
Error checking is not provided, except where needed for the program to compile.

Each language has a README file with more specific details for the language.

## Client program
The client programs are provided the IP Address and the Port number of the server that they will try to connect to.
When they have connected to a server, the program will take a user input and will send that to the server.
The response from the server will be displayed before the program will take any input again.

## Server program
The server programs start a server, with a given port number, that looks for a client making a connection.
When a client connects, the server will read what is sent and then respond to the message with "Server received:" followed by the message that was received.
This will repeat until the end message is received, this is "END" in these examples but can be easily changed.
