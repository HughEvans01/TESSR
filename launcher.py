#Get dependencies
import os
import socket

def wifiConnected():
    #Check if connected to internet
    try:
        #Test connection
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False

def updateSource():
    #Get latest build from GitHub repo
    os.system("git pull https://github.com/HughEvans01/TESSR")

print("TESSR, The Extremely Small Security Robot")

#If possible update source code
if wifiConnected():
    updateSource()

#Run source code
os.system("python3 main.py")
