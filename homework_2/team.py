#!/usr/bin/env python
import pika
import threading

# Producer - wysyla zlecenia
# Ekipy zamawiaja sprzet

# channel.basicQos(10) -> moze byc max 10 unacknowledged messages w tym kanale


def callback(channel, method, properties, body):
    print("[x] Received " + str(body.decode()))


def initialize_connection_and_exchange():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange='Expedition', exchange_type='topic')
    return connection, channel


def admin_stuff():
    connection, channel = initialize_connection_and_exchange()
    channel.queue_declare('lol', durable=True)
    channel.queue_bind(exchange='Expedition',
                       queue='lol',
                       routing_key='teams.*')

    channel.basic_consume(queue='lol',
                          on_message_callback=callback,
                          auto_ack=True)
    channel.start_consuming()



def order_stuff():
    connection, channel = initialize_connection_and_exchange()
    try:
        print("Team's name: ")
        team_name = input()

        channel.queue_declare(team_name, durable=True)
        channel.queue_bind(exchange='Expedition',
                        queue=team_name,
                        routing_key="order." + team_name)
        channel.queue_bind(exchange='Expedition',
                        queue=team_name,
                        routing_key="team.*")
        channel.queue_bind(exchange='Expedition',
                        queue=team_name,
                        routing_key='all.*')

        print("Order (you can order oxygen, boots, pack):")
        while (1):
            order = input()
            if order == 'oxygen':
                msg = team_name + ' oxygen'
                channel.basic_publish(exchange='Expedition',
                                    routing_key='order.oxygen',
                                    body=msg)
            elif order == 'boots':
                msg = team_name + ' boots'
                channel.basic_publish(exchange='Expedition',
                                    routing_key='order.boots',
                                    body=msg)
            elif order == 'pack':
                msg = team_name + ' pack'
                channel.basic_publish(exchange='Expedition',
                                    routing_key='order.pack',
                                    body=msg)
            else:
                print("Wrong input")
    except:
        print('Byee')
        channel.close()





def do_team_stuff():
    order_thread = threading.Thread(target = order_stuff)
    admin_thread = threading.Thread(target = admin_stuff)

    order_thread.start()
    admin_thread.start()



if __name__ == '__main__':
    do_team_stuff()
