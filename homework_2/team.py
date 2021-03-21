#!/usr/bin/env python
import pika
import threading

# Producer - wysyla zlecenia
# Ekipy zamawiaja sprzet

# channel.basicQos(10) -> moze byc max 10 unacknowledged messages w tym kanale


def callback(channel, method, properties, body):
    print(body.decode())


def initialize_connection_and_exchange():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange='Expedition', exchange_type='topic')
    return connection, channel


def admin_stuff(team_name):
    connection, channel = initialize_connection_and_exchange()
    channel.queue_declare(team_name, durable=True)
    channel.queue_bind(exchange='Expedition',
                       queue=team_name,
                       routing_key='teams.*')
    channel.queue_bind(exchange='Expedition',
                        queue=team_name,
                        routing_key='all.*')

    channel.basic_consume(queue=team_name,
                          on_message_callback=callback,
                          auto_ack=True)
    channel.start_consuming()



def order_stuff(team_name):
    connection, channel = initialize_connection_and_exchange()

    channel.queue_declare(team_name, durable=True)
    channel.queue_bind(exchange='Expedition',
                    queue=team_name,
                    routing_key="order." + team_name)


    print("Order (you can order oxygen, boots, pack):")
    while (1):
        order = input()
        if order == 'oxygen':
            msg = team_name + ' oxygen'
            channel.basic_publish(exchange='Expedition',
                                routing_key='order.oxygen',
                                properties=pika.BasicProperties(expiration='60000',),
                                body=msg)
        elif order == 'boots':
            msg = team_name + ' boots'
            channel.basic_publish(exchange='Expedition',
                                routing_key='order.boots',
                                properties=pika.BasicProperties(expiration='60000',),
                                body=msg)
        elif order == 'pack':
            msg = team_name + ' pack'
            channel.basic_publish(exchange='Expedition',
                                routing_key='order.pack',
                                properties=pika.BasicProperties(expiration='60000',),
                                body=msg)
        else:
            print("Wrong input")






def do_team_stuff():
    
    print("Team's name: ")
    team_name = input()
    
    order_thread = threading.Thread(target = order_stuff, args=(team_name,))
    admin_thread = threading.Thread(target = admin_stuff, args=(team_name,))

    order_thread.start()
    admin_thread.start()



if __name__ == '__main__':
    do_team_stuff()
