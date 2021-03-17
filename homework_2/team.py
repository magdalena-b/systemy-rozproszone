#!/usr/bin/env python
import pika

# Consumer

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host = 'localhost')
)

channel = connection.channel()

def callback(channel, method, properties, body):
    print("[x] Received " + str(body))


channel.basic_consume(
    queue = 'h', on_message_callback = callback, auto_ack = True
)

print('[*] Waiting for messages, to exit press ctrl + c')
channel.start_consuming()
