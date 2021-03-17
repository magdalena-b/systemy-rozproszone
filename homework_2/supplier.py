#!/usr/bin/env python
import pika

# Consumer - odbiera zlecenia
# Dostawca posiada liste dostepnych produktow
# 1. dostawca -> tlen, buty; 2. dostawca -> tlen, plecak


def initialize_everything(queue_name, routing_key, message_body, exchange = ''):
    
    connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))

    channel = connection.channel()
    channel.queue_declare(queue = queue_name)
    channel.basic_publish(exchange = '', routing_key = routing_key, body = message_body)
    return connection, channel

def do_supplier_stuff():
    connection, channel = initialize_everything('halo', 'halo', 'halo wieje halny')
    channel.close()


if __name__ == '__main__':
    do_supplier_stuff()



