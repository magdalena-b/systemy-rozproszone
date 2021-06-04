import sys
import Ice
Ice.loadSlice('../../../../slice/hello.ice')
import Hello


if __name__ == '__main__':
    with Ice.initialize(['--Ice.Config=config.client']) as communicator:
        base = communicator.stringToProxy('recommendMusic' + ":tcp -h localhost -p 10000")
        music_proxy = Hello.IRecommendMusicPrx.checkedCast(base)
        if not music_proxy:
            print("error")
        else:
            print("all good")
        #
        # while True:
        #     line = input()
        #     if line == "hello":
        #         # base = communicator.stringToProxy('machines/chocolateMachine' + ":tcp -h localhost -p 10000")
        #         # chocolate_proxy = Hello.IChocolateMachinePrx.checkedCast(base)
        #         music_proxy.recommendMusic("New Order");
