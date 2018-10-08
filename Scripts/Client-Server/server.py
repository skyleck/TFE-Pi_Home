import socket

hote = ''
port = 12800

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((hote, port))
server.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))

client, infos_connexion = server.accept()

action= b""
action= client.recv(1024)
print(action.decode())

print("Fermeture de la connexion")
client.close()
server.close()