#!/usr/bin/env python
import pika


# Admin wysyla 3 wiadomosci do:
# ALL ekipy
# ALL dostawcy
# ALL (ekipy i dostawcy)

def do_admin_stuff():
    pass


if __name__ == '__main__':
    do_admin_stuff()



# #!/usr/bin/env python
# import pika

# # Consumer - odbiera zlecenia
# # Dostawca posiada liste dostepnych produktow
# # 1. dostawca -> tlen, buty; 2. dostawca -> tlen, plecak


# def initialize_everything(queue_name, routing_key, message_body, exchange = ''):
    
#     connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))

#     channel = connection.channel()
#     channel.queue_declare(queue = 'Everest')
#     channel.basic_publish(exchange = '', routing_key = 'halo', body = 'halo wieje halny')
#     return connection, channel

# def do_supplier_stuff():
#     connection, channel = initialize_everything('Everest', 'halo', 'halo wieje halny')
#     channel.close()


# if __name__ == '__main__':
#     do_supplier_stuff()
