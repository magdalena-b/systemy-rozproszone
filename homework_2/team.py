#!/usr/bin/env python
import pika

# Producer - wysyla zlecenia
# Ekipy zamawiaja sprzet

# channel.basicQos(10) -> moze byc max 10 unacknowledged messages w tym kanale

admin_exchange_name = 'Admin'
teams_exchange_name = 'Teams'
suppliers_exchange_name = 'Suppliers'


def callback(channel, method, properties, body):
    print("[x] Received " + str(body.decode()))


def place_an_order():
    pass


def initialize_everything():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
    channel = connection.channel()
    # channel.basic_consume(queue = 'halo', on_message_callback = callback, auto_ack = True)
    # channel.start_consuming()


def do_team_stuff():
    connection, channel = initialize_everything()
    
    # admin_thread
    while(1):
        # zlecaj


if __name__ == '__main__':
    do_team_stuff()

