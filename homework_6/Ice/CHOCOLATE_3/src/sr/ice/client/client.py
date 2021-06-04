import sys
import Ice
Ice.loadSlice('../../../../slice/hello.ice')
import Hello


if __name__ == '__main__':
    with Ice.initialize(['--Ice.Config=config.client']) as communicator:
        # base = communicator.stringToProxy('machines/chocolateMachine' + ":tcp -h localhost -p 10000")
        # chocolate_proxy = Hello.IChocolateMachinePrx.checkedCast(base)
        # if not chocolate_proxy:
        #     print("error")
        # else:
        #     print("all good")

        while True:
            line = input()
            if line == "hello":
                base = communicator.stringToProxy('machines/chocolateMachine' + ":tcp -h localhost -p 10000")
                chocolate_proxy = Hello.IChocolateMachinePrx.checkedCast(base)
                chocolate_proxy.makeChocolate("MILK", 100)

            if line == "tea":
                base = communicator.stringToProxy('machines/teaMachine' + ":tcp -h localhost -p 10000")
                tea_proxy = Hello.ITeaMachinePrx.checkedCast(base)
                tea_proxy.makeTea("SENCHA", 100, 10);
