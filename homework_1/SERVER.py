import socket
import threading


server_port = 9015

clients = []

def listen_to_client(client_id):
    
    client = clients[client_id]

    while True:
        prefix_msg = 'Friend ' + str(client_id) + ": "
        rcv_msg = client.recv(1024).decode('utf-8')
        msg = prefix_msg + rcv_msg
        for c in clients:
            if c == client:
                continue
            c.send(msg.encode('utf-8'))


def listen_to_client_UDP(UDP_socket):

    while True:
        msg, client = UDP_socket.recvfrom(1024)
        for c in clients:
            if c == client:
                continue
            c.send(msg)


def do_server_stuff():
    
    TCP_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCP_socket.bind(('localhost', server_port))
    TCP_socket.listen()

    UDP_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UDP_socket.bind(('localhost', server_port))

    udp_thread = threading.Thread(target=listen_to_client_UDP, args=(UDP_socket,))
    udp_thread.start()
    client_id = 0

    print("Chat™ is readyy")
    while True:

        just_connected_client, addr = TCP_socket.accept()
        clients.append(just_connected_client)

        thread = threading.Thread(target=listen_to_client, args=(client_id,))
        client_id += 1
        thread.start()


if __name__ == '__main__':
    do_server_stuff()
