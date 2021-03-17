#!/usr/bin/env python
import pika

# Producer

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host = 'localhost')
)

channel = connection.channel()
channel.queue_declare(queue = 'Everest')
channel.basic_publish(exchange = '', routing_key = 'halo', body = 'halo wieje halny')
channel.close()

