#Programmimng our first client
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Create a socket for communicationg with the server
print("Socket created")
PORT=8080
IP= "212.128.253.64"
# Connect to the server
s.connect((IP,PORT))
s.send(str.encode("HELLO FROM MY CLIENT"))
msg= s.recv(2048).decode("utf-8")
print("MESSAGE FROM THE SERVER:")
print(msg)
s.close()


print("The end")
