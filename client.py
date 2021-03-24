import socket

#length of the bytes from client for the message to be sent.
HEADER = 64
#get a port
PORT = 5500
#get the address to make it as server
SERVER = socket.gethostbyname(socket.gethostname()) 
#bind() accepts tuple only as arguments
ADDR = (SERVER,PORT)
# utf-8 is a format that converts from bytes to strings
FORMAT = "utf-8"
# proper disconnection of client is important because if not then there might be an issue during reconnection.
DISCONNECT_MESSAGE = "!DISCONNECT"


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#connecting to the server
client.connect(ADDR)

def send(msg):
    #send the length of the message padded with 64, and then send the actual message 
    message=msg.encode(FORMAT)
    msg_length=len(message) 
    send_length = str(msg_length).encode(FORMAT)
    #Padding it to 64 bytes because that is the format we decided for server as well.
    send_length+= b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("Hllo world")
input()
send("Hey MJ")
input()

send(DISCONNECT_MESSAGE)
