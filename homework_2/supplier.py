#!/usr/bin/env python
import pika
import time
import threading

# Consumer - odbiera zlecenia
# Dostawca posiada liste dostepnych produktow
# 1. dostawca -> klucze: tlen, buty; 2. dostawca -> klucze: tlen, plecak

# zlecenia identyfikowane sa przez nazwe Teamu oraz wewnetrzny
# numer zlecenia nadany przez Suppliera


def callback(channel, method, properties, body):
    print("[x] Received " + str(body.decode()))


def execute_order(channel, method, properties, body):

    print("Received order: " + body.decode())
    print("Working hard")
    time.sleep(1)
    channel.basic_ack(delivery_tag = method.delivery_tag)
    # basicPublish("elo zrobione")


def initialize_connection_and_exchange():

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange='Expedition', exchange_type='topic')
    return connection, channel



def admin_stuff(supplier_name):
    connection, channel = initialize_connection_and_exchange()
    channel.queue_declare(supplier_name, durable=True)
    channel.queue_bind(exchange='Expedition',
                       queue=supplier_name,
                       routing_key='suppliers.*')
    channel.queue_bind(exchange='Expedition',
                        queue=supplier_name,
                        routing_key='suppliers.*')
    channel.queue_bind(exchange='Expedition',
                        queue=supplier_name,
                        routing_key='all.*')

    channel.basic_consume(queue=supplier_name,
                          on_message_callback=callback,
                          auto_ack=True)
    channel.start_consuming()


def order_stuff(supplier_name):
    connection, channel = initialize_connection_and_exchange()

    try:
        print("Available products (oxygen, boots, pack): ")
        products_input = input()
        products = list(products_input.split(" "))
        # print(products)

        for product in products:
            channel.queue_declare(queue=product, durable=True)
            channel.queue_bind(exchange='Expedition',
                            queue=product,
                            routing_key='order.' + product)

        channel.basic_qos(prefetch_count=1)  # rownowazenie obciazenia

        channel.queue_declare(queue=supplier_name, durable=True)


        for product in products:
            channel.basic_consume(queue=product,
                                on_message_callback=execute_order)

        channel.basic_consume(queue=supplier_name,
                            on_message_callback=execute_order)
        channel.start_consuming()
    except:
        print('Byee')
        channel.close()        


def do_supplier_stuff():
    
    print("Supplier's name: ")
    supplier_name = input()

    order_thread = threading.Thread(target = order_stuff, args=(supplier_name,))
    admin_thread = threading.Thread(target = admin_stuff, args=(supplier_name,))

    order_thread.start()
    admin_thread.start()


if __name__ == '__main__':
    do_supplier_stuff()







