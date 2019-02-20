# the client is going to send a message introduced by the user by an input, this message is going to be introducing in different lines first the sequence and then the method and when the user introduces a blank line it will be en the input. it is as indicator
import socket

# SERVER IP, PORT
PORT = 8089
IP = "127.0.0.1"


while True:

    # Before connecting to the server, ask the user for the string
    enviar = ""
    msg = input(">")
    while len(msg) > 0:
        enviar= enviar + msg + "\n"
        msg = input(">")

    if len(enviar) == 0:
        enviar = "\n"



    # Now we can "create the socket and connect to the servewr
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send the request message to the server
    s.send(str.encode(enviar))

    # Receive the servers respoinse
    response = s.recv(2048).decode()

    # Print the server's response
    print("Response: {}".format(response))

    s.close()