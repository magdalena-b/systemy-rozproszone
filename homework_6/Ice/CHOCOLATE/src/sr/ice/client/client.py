import sys
import Ice
Ice.loadSlice('../../../../slice/smarthome.ice')
import SmartHome


if __name__ == '__main__':
    with Ice.initialize(['--Ice.Config=config.client']) as communicator:
        base = communicator.stringToProxy('machines/chocolateMachine' + ":tcp -h localhost -p 10000")
        chocolate_proxy = SmartHome.IChocolateMachinePrx.checkedCast(base)
        if not chocolate_proxy:
            print("error")
        else:
            print("all good")