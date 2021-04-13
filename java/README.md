# Java

## Notes
There is basic error handling in these programs, so that they would compile. The Client class has UnknownHostException handling to handle if there is not a server at the IP Address using the port. Both classes have IOException handling to handle if there is a problem when creating the BufferedReader and BufferedWriter used to send and receive data or if there is a problem when sending or receiving data.

## Client
The client gets the IP Address and Port number from command line arguments, to run use ```$ java Client <IP Address> <Port Number>``` after compiling.

## Server
The server gets the Port number from command line arguments, to run use ```$ java Server <Port Number>``` after compiling.
