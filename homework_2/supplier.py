#!/usr/bin/env python
import pika

# Consumer - odbiera zlecenia
# Dostawca posiada liste dostepnych produktow
# 1. dostawca -> klucze: tlen, buty; 2. dostawca -> klucze: tlen, plecak

# zlecenia identyfikowane sa przez nazwe Teamu oraz wewnetrzny
# numer zlecenia nadany przez Suppliera


admin_exchange_name = 'Admin'
teams_exchange_name = 'Teams'
suppliers_exchange_name = 'Suppliers'


def execute_order():
    print("Working hard")
    sleep(1)
    # basicPublish("elo zrobione")


def initialize_everything():
    
    connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))

    channel = connection.channel()
    channel.exchange_declare(exchange = 'Expedition', exchange_type = 'topic')
    # channel.basic_publish(exchange = '', routing_key = routing_key, body = message_body)
    return connection, channel

def do_supplier_stuff():
    connection, channel = initialize_everything()
    
    print("Supplier's name: ")
    name = input()
    print("Available products (oxygen, boots, pack): ")
    products_input = input()
    products = list(products_input.split(" "))
    # print(products)

    # admin_thread
    # osobny thread na nasluchiwanie zlecen na kazdy available product
    
    for product in products:
        channel.queue_declare(queue = product, durable = True)
        channel.queue_bind(exchange = 'Expedition', queue = product) # bindowanie kolejki do exchange'a

    channel.basic_qos(prefetch_count = 1) # rownowazenie obciazenia

    channel.queue_declare(queue = queue_name, durable = True)



    
    channel.close()


if __name__ == '__main__':
    do_supplier_stuff()



