#!/usr/bin/env python
import pika
import threading

message_type = ['teams', 'suppliers', 'everyone']

# channel.queue_bind(exchange = exchange_name, queue = queue_name, routing_key = "bla.*")
# What the code is telling: I, "queue_name", am interested in the message from "exchange_name".

# Admin wysyla 3 wiadomosci do:
# ALL ekipy
# ALL dostawcy
# ALL (ekipy i dostawcy)

# dostaje kopie ALL wysylanych wiadomosci w systemie
# exchange_admin, exchange_normal


def callback(channel, method, properties, body):
    print("[x] Received " + str(body.decode()))


def take_input():
    print(
        "Choose type of message to be sent:\nTo all teams: 1\nTo all suppliers: 2\nTo everyone: 3"
    )
    msg_type_option = input()
    return msg_type_option


def translate_input(option):
    x = int(option)
    if x == 1:
        return message_type[0]
    elif x == 2:
        return message_type[1]
    elif x == 3:
        return message_type[2]
    else:
        print('Wrong input')
        x2 = take_input()
        translate_input(x2)


def initialize_connection_and_exchange():

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange='Expedition', exchange_type='topic')
    return connection, channel


def send_messages():

    connection, channel = initialize_connection_and_exchange()
    while True:
        msg_type_option = take_input()
        msg_type = translate_input(msg_type_option)
        # print(msg_type)
        print('Your message to ' + msg_type + ': ')
        admin_msg_input = input()
        admin_msg = "Admin " + admin_msg_input

        if msg_type == 'teams':
            channel.basic_publish(exchange='Expedition',
                                  routing_key='teams.*',
                                  body=admin_msg)
        elif msg_type == 'suppliers':
            channel.basic_publish(exchange='Expedition',
                                  routing_key='suppliers.*',
                                  body=admin_msg)
        elif msg_type == 'everyone':
            channel.basic_publish(exchange='Expedition',
                                  routing_key='all.*',
                                  body=admin_msg)


def listen_to_messages():
    # admin nasluchuje skladania i potwierdzania zamowien
    connection, channel = initialize_connection_and_exchange()
    channel.queue_declare('admin', durable=True)
    channel.queue_bind(exchange='Expedition',
                       queue='admin',
                       routing_key='order.*')

    channel.basic_consume(queue='admin',
                          on_message_callback=callback,
                          auto_ack=True)
    channel.start_consuming()


def do_admin_stuff():

    send_messages_thread = threading.Thread(target=send_messages)
    listen_to_messages_thread = threading.Thread(target=listen_to_messages)

    send_messages_thread.start()
    listen_to_messages_thread.start()


if __name__ == '__main__':
    do_admin_stuff()
