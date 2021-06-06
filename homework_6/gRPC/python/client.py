
from __future__ import print_function
import logging

import grpc
import threading

import helloworld_pb2 as helloworld_pb2
import helloworld_pb2_grpc as helloworld_pb2_grpc



def get_cities():

    cities = list()

    print("Zapisz się na powiadomenia o zawodach w miastach (możesz wybrać kilka): ")
    print("1 - Kraków")
    print("2 - Poznań")
    print("3 - Warszawa")
    print("Przykładowy input: 1 2")
    print("Wybierz miasta: ")
    input_cities = input()
    chosen_cities = input_cities.split(" ")

    for city in chosen_cities:
        if city == "1":
            cities.append("Krakow")
        elif city == "2":
            cities.append("Poznan")
        elif city == "3":
            cities.append("Warszawa")
        else:
            print("Nieprawidłowy input")
            cities = get_cities()

    return cities


def get_categories():

    categories = list()

    print("Zapisz się na powiadomenia o zawodach w dyscyplinach (możesz wybrać kilka): ")
    print("1 - Boks")
    print("2 - Kickboxing formuła K1")
    print("3 - Kickboxing formuła Low Kick")
    print("4 - Kickboxing formuła Kick Light")
    print("5 - Muay Thai")
    print("Przykładowy input: 1 2 5")
    print("Wybierz dyscypliny: ")
    input_categories = input()
    chosen_categories = input_categories.split(" ")

    for category in chosen_categories:
        if category == "1":
            categories.append("Boks")
        
        elif category == "2":
            categories.append("K1")
        
        elif category == "3":
            categories.append("Low_Kick")

        elif category == "4":
            categories.append("Kick_Light")

        elif category == "5":
            categories.append("Muay_Thai")
        
        else:
            print("Nieprawidłowy input")
            categories = get_categories()

    return categories


def get_event():

    print("Wybierz typ zawodów (tylko jeden):")
    print("1 - amatorskie")
    print("2 - zawodnicze")
    input_event = input()

    if input_event == "1":
        event = helloworld_pb2.Event.AMATEUR
    elif input_event == "2":
        event = helloworld_pb2.Event.ATHLETE
    else:
        print("Nieprawidłowy input")
        event = get_event()

    return event


    


def run():

    cities = get_cities()
    categories = get_categories()
    event = get_event()

    subscription = helloworld_pb2.Subscription(city=cities, category=categories, event=event)

    try:
        while True:
            with grpc.insecure_channel('0.0.0.0:50051') as channel:
                stub = helloworld_pb2_grpc.NotificatorStub(channel)

                try:
                    iterator = stub.subscribe(subscription)
                    for notification in iterator:
                        print(notification.message)

                    print('Server disconnected gracefully')

                except grpc.RpcError as e:
                    status_code = e.code()

                    if e.details() == 'Stream removed':
                        print('Server disconnected, trying to reconnect...')
                        pass

                    elif status_code == grpc.StatusCode.UNAVAILABLE:
                        print('Server unavailable')

                    else:
                        print(e)
                        raise SystemExit

    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    run()

