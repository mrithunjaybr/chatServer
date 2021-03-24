import socket
import threading


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

#creating a socket and binding the ip4 address with a port, so that a client only hits this port and address.
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handleClients(conn, addr):
    #handle each client concurrently
    print(f"[NEW CONNECTION] : {addr} connected.")
    connected = True
    while connected:
        # recv a message from the client
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:

            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected=False
            print(f"{addr} : {msg}")

            conn.send("Message Received...".encode(FORMAT))

    conn.close()





def start():
    # starts running the server and accepts new connections from clients.
    server.listen()
    print(f"[THE SERVER IS LISTENTING ON : {SERVER}]")
    while True:
        # conn is the socket from client side and addr is the address of the client.
        conn, addr = server.accept()
        print(f"SERVER SIDE : {conn,addr}")
        #threading makes sure handleClients() has several number of threads running concurrently.
        thread = threading.Thread(target=handleClients,args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] : {threading.activeCount()- 1}")



print("[SERVER IS STARTING cdsfdsf]")
start()