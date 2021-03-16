import socket
import threading
import struct


TCP_socket_ip = '127.0.0.1'
TCP_socket_port = 9015

multicast_ip = '224.0.0.1'
multicast_port = 9009


def init_multicast():
    # tworzenie nowego gniazda multicast
    MULTICAST_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    MULTICAST_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    MULTICAST_socket.bind(('', multicast_port))

    # dodanie gniazda do grupy multicast
    group = socket.inet_aton(multicast_ip)
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    MULTICAST_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    return MULTICAST_socket



def receive(TCP_socket):
    
    while True:
        msg = TCP_socket.recv(1024).decode('utf-8')
        print(msg)


def receive_multicast(MULTICAST_socket):

    while True:
        msg, address = MULTICAST_socket.recvfrom(1024)
        print(msg.decode('utf-8'))



def send(TCP_socket, UDP_socket, MULTICAST_socket):

    while True:
        message = input()

        if message == 'U':
            with open('tranquility.txt', 'r') as file:
                UDP_socket.sendto(file.read().encode('utf-8'), (TCP_socket_ip, TCP_socket_port))
        elif message == 'M':
            with open('moomin.txt', 'r') as file:
                MULTICAST_socket.sendto(file.read().encode('utf-8'), (multicast_ip, multicast_port))
        else: 
            TCP_socket.send(message.encode('utf-8'))


def do_client_stuff():

    TCP_socket = socket.create_connection((TCP_socket_ip, TCP_socket_port))
    UDP_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    MULTICAST_socket = init_multicast()


    recv_thread = threading.Thread(target=receive, args=(TCP_socket,))
    send_thread = threading.Thread(target=send, args=(TCP_socket, UDP_socket, MULTICAST_socket,))
    multicast_thread = threading.Thread(target=receive_multicast, args=(MULTICAST_socket,))

    recv_thread.start()
    send_thread.start()
    multicast_thread.start()


if __name__ == '__main__':
    do_client_stuff()