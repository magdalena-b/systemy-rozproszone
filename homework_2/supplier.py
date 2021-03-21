#!/usr/bin/env python
import pika
import time
import threading

# Consumer - odbiera zlecenia
# Dostawca posiada liste dostepnych produktow
# 1. dostawca -> klucze: tlen, buty; 2. dostawca -> klucze: tlen, plecak

# zlecenia identyfikowane sa przez nazwe Teamu oraz wewnetrzny
# numer zlecenia nadany przez Suppliera


order_id = 0

def callback(channel, method, properties, body):
    print(body.decode())


def execute_order(channel, method, properties, body):
    
    global order_id

    msg = body.decode()

    if msg.find('Admin') == -1:
        order_id += 1
        print("Received order: " + body.decode())
        print("Working hard on order " + str(order_id))
        time.sleep(1)

        
        client_team, ordered_item = body.decode().split(' ')
        
        channel.basic_publish(exchange='Expedition',
                        routing_key = 'order.' + client_team,
                        properties=pika.BasicProperties(expiration='60000',),
                        body = 'Here is your order: ' + ordered_item)
        
        print("Done with order " + str(order_id))



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

    print("Available products (oxygen, boots, pack): ")
    products_input = input()
    products = list(products_input.split(" "))
    # print(products)

    for product in products:
        channel.queue_declare(queue=product, durable=True)
        channel.queue_bind(exchange='Expedition',
                        queue=product,
                        routing_key='order.' + product)

    channel.basic_qos(prefetch_count = 10)  # rownowazenie obciazenia

    channel.queue_declare(queue=supplier_name, durable=True)


    for product in products:
        channel.basic_consume(queue=product,
                            on_message_callback=execute_order,
                            auto_ack=True)

    channel.basic_consume(queue=supplier_name,
                        on_message_callback=execute_order,
                        auto_ack=True)
    channel.start_consuming()
       


def do_supplier_stuff():
    
    print("Supplier's name: ")
    supplier_name = input()

    order_thread = threading.Thread(target = order_stuff, args=(supplier_name,))
    admin_thread = threading.Thread(target = admin_stuff, args=(supplier_name,))

    order_thread.start()
    admin_thread.start()


if __name__ == '__main__':
    do_supplier_stuff()







