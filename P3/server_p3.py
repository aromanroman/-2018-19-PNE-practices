#we are going to create a server very special that consist that it will receive a sequence and methods from the client. The server has to analyze the sequence and send the
# information to the client according to the methods that the client have ask, in case that the method does not exist or the sequence is not valid the
# server has to send "ERROR"
import socket
import termcolor
from Seq import Seq
import sys
# Configure the Server's IP and PORT
PORT = 8089
IP = "127.0.0.1"
MAX_OPEN_REQUESTS = 5

def validSequene(s):
    valid ="ACTG"
    for letter in s:
        if letter not in valid:
            return False
    return True
def tratar(s1, comando):
    print("haciendo comando", comando)
    if comando == "len":
        return s1.len()
    elif comando == "complement":
        return s1.complement().get_strbase()
    elif comando == "reverse":
        return s1.reverse().get_strbase()
    elif comando == "countT":
        return s1.count("T")
    elif comando == "countA":
        return s1.count("A")
    elif comando == "countG":
        return s1.count("G")
    elif comando == "countC":
        return s1.count("C")
    elif comando == "percA":
        return s1.perc("A")
    elif comando =="percT":
        return s1.perc("T")
    elif comando == "percG":
        return s1.perc("G")
    elif comando == "percC":
        return s1.perc("C")


def process_client(cs):
    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")



    # Print the received message, for debugging
    termcolor.cprint("Hey! this is printed in green!", 'green')

    if msg == "\n":
        response = "alive"
    else:
        pieces = msg.split("\n")
        print("Valorando", pieces[0])
        if validSequence(pieces[0]):
            response = "OK\n"
            s1 = Seq(pieces[0])
            for i in range(1, len(pieces)-1):
                print("Tratando el comando", i, pieces[i])
                r = tratar(s1, pieces[i])
                response = response+str(r)+"\n"
        else:
            response = "ERROR"



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

    # Service the client
    process_client(clientsocket)