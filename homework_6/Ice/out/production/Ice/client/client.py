import sys
import Ice
Ice.loadSlice('../../slice/hello.ice')
import Hello


def get_commands():
    print("Available commands: \n help - print this message \n music - recommend music "
           + "\n panda - get panda fact \n koala - get koala fact"
          + "\n lyrics - get lyrics to a given song "
          + "\n timer - set timer for a given time"
          + "\n random int - random int in a given range"
          + "\n random double - random double in a given range")


if __name__ == '__main__':
    with Ice.initialize(['--Ice.Config=config.client']) as communicator:

        base_api = communicator.stringToProxy('getAPI' + ":tcp -h localhost -p 10000")
        api_proxy = Hello.IGetAPIPrx.checkedCast(base_api)

        base_random = communicator.stringToProxy('getRandomNumber' + ":tcp -h localhost -p 10000")
        random_proxy = Hello.IGetRandomNumberPrx.checkedCast(base_random)

        get_commands()

        while True:
            line = input()

            if line == "help":
                get_commands()


            elif line == "music":
                base_music = communicator.stringToProxy('recommendMusic' + ":tcp -h localhost -p 10000")
                music_proxy = Hello.IRecommendMusicPrx.checkedCast(base_music)
                print(music_proxy.recommendMusic())

            elif line == "panda":
                try:
                    print(api_proxy.getPandaFact())
                except:
                    print("Sorry, try again")

            elif line == "koala":
                try:
                    print(api_proxy.getKoalaFact())
                except:
                    print("Sorry, try again")

            elif line == "lyrics":
                print("Title: ")
                title = input()
                print("Artist: ")
                artist = input()
                try:
                    print(api_proxy.getLyrics(title, artist))
                except:
                    print("Song not found")

            elif line == "timer":
                base_timer = communicator.stringToProxy('setTimer' + ":tcp -h localhost -p 10000")
                timer_proxy = Hello.ISetTimerPrx.checkedCast(base_timer)
                print("Time (in seconds):")
                time = input()
                try:
                    print(timer_proxy.setTimer(time))
                except:
                    print("Wrong number input")

            elif line == "random int":
                print("Min: ")
                min = input()
                print("Max: ")
                max = input()
                print(random_proxy.getRandomInt(min, max))
                # try:
                #     print(random_proxy.getRandomInt(min, max))
                # except:
                #     print("Wrong number input")


            elif line == "random double":
                print("Min: ")
                min = input()
                print("Max: ")
                max = input()
                try:
                    print(random_proxy.getRandomDouble(min, max))
                except:
                    print("Wrong number input")

            else:
                print("Wrong command, try again (or use to see available commands")

