# the server has to receive a message from the client and that message will be send to the client, that is why the nane of echo_server
import socket
import termcolor
import sys
# Configure the Server's IP and PORT
PORT = 8089
IP = "127.0.0.1"
MAX_OPEN_REQUESTS = 5


def process_client(cs):
    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""
    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")
    if msg == "EXIT":
        sys.exit(0)
    # Print the received message, for debugging
    termcolor.cprint("Hey! this is printed in green!", 'green')
    print("Request message: {}".format(msg))
    # Send the msg back to the client (echo)
    cs.send(str.encode(msg))
    # Close the socket
    cs.close()


# MAIN PROGRAM
# create an INET, STREAMing socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and PORT
serversocket.bind((IP, PORT))
# Configure the server sockets
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
serversocket.listen(MAX_OPEN_REQUESTS)
print("Socket ready: {}".format(serversocket))
while True:
    # accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()
    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))
    # service the client
    process_client(clientsocket)
