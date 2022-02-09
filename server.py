##########################################################
################### IMPORT ###############################
########################################################## 
from concurrent.futures import thread
from threading import Thread
import socket
import time


##########################################################
################### MÉTHODE ##############################
########################################################## 
def Send(client, msg):
    msg = msg.encode("utf-8")
    client.send(msg)

def SendAllPlayer(instances, msg):
    for player in instances:
        Send(player[0], msg)
    
def Reception(client):
    requete_client = client.recv(500)
    requete_client = requete_client.decode('utf-8')
    return requete_client

def ReceptionUsername(usernames, i, client):
    requete_client = client.recv(500)
    requete_client = requete_client.decode('utf-8')
    usernames[i]=requete_client

# GET ALL USER CONNECTION
def NewClient(nb_player_total):
    nb_player = 0
    while nb_player != nb_player_total:
        
        socket.listen(1)
        
        #Le script s'arrête jusqu'a une connection
        client, ip = socket.accept()
        instances.append([client, ip])
        
        print("Le client d'ip",ip,"s'est connecté")
        nb_player+=1

######################################################### 
################### INITIALISATION SOCKET ###############
######################################################### 
Host = "192.168.1.69"
Port = 6390

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.bind((Host,Port))

######################################################### 
################### MAIN PART ###########################
#########################################################

################### Get all connection ##################


instances = []
NewClient(2) #Number of player
maintener = instances[0][0]

SendAllPlayer(instances, '1')

################### Get username ########################
i=0
SendAllPlayer(instances, '3')

usernames = [None] * len(instances) #List of username

#Create all thread
threads=[]
for player in instances:
    threads.append(Thread(target=ReceptionUsername,args=(usernames, i, player[0])))
    i+=1

#Start all thread
for thread in threads:
    thread.start()

#wait all thread
for thread in threads:
    thread.join()
    
SendAllPlayer(instances, '101')
print(usernames)

################### Get role ###########################

Send(instances[0][0], '2')
time.sleep(50)
socket.close()