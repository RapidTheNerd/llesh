import os
import socket
import subprocess

def socketMake():
    try:
        global host
        global port
        global s
        host ="should rename this!"
        port = 9999
        s = socket.socket()
    except socket.error as msg:
            print(msg)

def socketConnect():
    try:
        global host
        global port
        global s
        s.connect((host, port))
    except socket.error as msg:
        print(msg)

        
