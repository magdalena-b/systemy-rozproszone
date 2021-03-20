#!/usr/bin/env python
import pika
import threading

# Producer - wysyla zlecenia
# Ekipy zamawiaja sprzet

# channel.basicQos(10) -> moze byc max 10 unacknowledged messages w tym kanale


def callback(channel, method, properties, body):
    print("[x] Received " + str(body.decode()))


def place_an_order(channel):

        print("Order: (you can order oxygen, boots, pack")
        while(1):
        order = input()
        if order == 'oxygen':
            msg = team_name + ' oxygen'
            channel.basic_publish(exchange = 'Expedition', routing_key = 'order.oxygen', body = msg)
        elif order == 'boots':
            msg = team_name + ' pack'
            channel.basic_publish(exchange = 'Expedition', routing_key = 'order.boots', body = msg)
        elif order == 'pack':
            msg = team_name + ' pack'
            channel.basic_publish(exchange = 'Expedition', routing_key = 'order.pack', body = msg)
        else:
            print("Wrong input")


def initialize_connection_and_exchange():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
    channel.exchange_declare(exchange = 'Expedition', exchange_type = 'topic')    
    channel = connection.channel()


def do_team_stuff():
    connection, channel = initialize_connection_and_exchange()
    print("Team's name: ")
    team_name = input()

    order_thread = threading.Thread(target = place_an_order, args=(channel,))

    channel.queue_declare(team_name, durable = True)
    channel.queue_bind(exchange = 'Expedition', queue = team_name, routing_key = "order." + team_name)
    channel.queue_bind(exchange = 'Expedition', queue = team_name, routing_key = "team.*")


if __name__ == '__main__':
    do_team_stuff()

