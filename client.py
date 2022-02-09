from threading import Thread
import socket
import time

def Send(socket, msg):
    msg = msg.encode('utf-8')
    socket.send(msg)
        
def Reception(socket):
    requete_server = socket.recv(500)
    requete_server = requete_server.decode("utf-8")
    return requete_server

Host = "192.168.1.69"
Port = 6390

#Création du socket
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect((Host,Port))

code = int(Reception(socket))

'''
CODE DE RECEPTION
-1 : Erreur
0 : Exit
1 : Check all player
2 : waiting role
3 : ask username

101 : Waiting Maintener
102 : Waiting xxx
103 : Waiting xxx
'''

while(code != 0):
    print("##############")
    if code == 1:
        print("Tout les joueurs sont connectés")
        
    elif code == 2:
        print("En attente des rôles")
        
    elif code == 3:
        print("Ask username")
        username=input()
        Send(socket, username)
        print("Hey ", username," !")
        print("Wait other player...")
    
    elif code == 101:
        print("Wait maintener... \nMaking roles")
        
        
    code = int(Reception(socket))

time.sleep(50)
