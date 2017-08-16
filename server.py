import socket
import sys

def create():
    try:
        global host
        global port
        global st
        host = ""
        port = 999
        s = socket.socket()
    except socket.error as msg:
        print("Socket error")