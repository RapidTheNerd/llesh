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

def bindSocket():
           try:
               global host
               global port
               global s
               print("binding socket")
              #bind
           except socket.error as msg:
               print("socket binding error:" + msg)
               
