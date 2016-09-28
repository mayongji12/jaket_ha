#socket_client.py

import socket

def socket_send(command):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((master, master_port))
    sock.send(command)
    result = sock.recv(2048)
    sock.close()
    return result

if __name__ == '__main__':
    cmd = "df -h"
    print socket_send(cmd)
