#!/usr/bin/env python
import pika

message_type = ['teams', 'suppliers', 'everyone']

# Admin wysyla 3 wiadomosci do:
# ALL ekipy
# ALL dostawcy
# ALL (ekipy i dostawcy)

# dostaje kopie ALL wysylanych wiadomosci w systemie
# exchange_admin, exchange_normal


def take_input():
    print("Choose type of message to be sent:\nTo all teams: 1\nTo all suppliers: 2\nTo everyone: 3")
    msg_type_option = input()
    return msg_type_option


def translate_input(option):
    x = int(option)
    if x == 1:
        return message_type[0]
    elif x == 2:
        return message_type[1]
    elif x == 3:
        return message_type[2]
    else:
        print('Wrong input')
        x2 = take_input()
        translate_input(x2)

def do_admin_stuff():
    msg_type_option = take_input()
    msg_type = translate_input(msg_type_option)
    # print(msg_type)
    print('Your message to ' + msg_type + ': ')
    admins_msg = input()
    # publish message to the right channel


if __name__ == '__main__':
    do_admin_stuff()




