#!/usr/bin/env python
import pika

# Consumer - odbiera zlecenia
# Dostawca posiada liste dostepnych produktow
# 1. dostawca -> klucze: tlen, buty; 2. dostawca -> klucze: tlen, plecak

# zlecenia identyfikowane sa przez nazwe Teamu oraz wewnetrzny
# numer zlecenia nadany przez Suppliera


def executr_order():
    print("Working hard")
    sleep(1)
    # basicPublish("elo zrobione")


def initialize_everything(queue_name, routing_key, message_body, exchange = ''):
    
    connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))

    channel = connection.channel()
    channel.queue_declare(queue = queue_name)
    channel.basic_publish(exchange = '', routing_key = routing_key, body = message_body)
    return connection, channel

def do_supplier_stuff():
    connection, channel = initialize_everything('halo', 'halo', 'halo wieje halny')
    
    print("Supplier's name: ")
    name = input()
    print("Available products (oxygen, boots, pack): ")
    products_input = input()
    products = list(products_input.split(" "))
    print(products)

    # admin_thread
    # osobny thread na nasluchiwanie zlecen na kazdy available product
    
    
    channel.close()


if __name__ == '__main__':
    do_supplier_stuff()



