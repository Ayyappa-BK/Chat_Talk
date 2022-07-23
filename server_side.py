from os import remove
import socket
import select
import sys
from _thread import *

from numpy import broadcast

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if(len(sys.argv)!=3):
    print("Correct usage is Script, IP Address, Port Number")
    exit()

IP_address=str(sys.argv[1])
Port=int(sys.argv[2])

server.bind(IP_address,Port)

server.listen(100)

list_of_clients=[]

def client_thread(conn, addr):
    conn.send("Welcome to the Chat_Talk!")
    while True:
        try:
            message=conn.recv(2048)
            if message:
                print("<"+addr[0]+"> "+message)
                messgae_to_send="<"+addr[0]+"> "+message
                broadcast(messgae_to_send)
            else:
                remove(conn)
        
        except:
            continue

       
def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)


while True:
    conn, addr=server.accept()
    list_of_clients.append(conn)
    print(addr[0]+" connected")
    start_new_thread(client_thread,(conn,addr))

conn.close()
server.close()