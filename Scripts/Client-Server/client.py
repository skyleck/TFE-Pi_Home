import socket

hote = "192.168.1.6" #a adapter
port = 12800

loginServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
loginServer.connect((hote, port))
print("Connexion etablie avec le serveur sur le port {}".format(port))

action = b"message"
action = action.encode()
loginServer.send(action)
msg_recu = loginServer.recv(1024)
print(msg_recu.decode())

print("Fermeture de la connexion")
loginServer.close()