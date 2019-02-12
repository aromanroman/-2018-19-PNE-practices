#Write a python client for implementing a chat. It should ask the user to enter a string and then sending the message to the Teacher's serve
import socket
IP="212.128.253.64"
PORT= 8081

while True:
    msg= input("write a message")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP,PORT))
    s.send(str.encode(msg))
    msg= s.recv(2048).decode("utf-8")
    print("MESSAGE FROM THE SERVER:")
    print(msg)
    s.close()


print("The end")
