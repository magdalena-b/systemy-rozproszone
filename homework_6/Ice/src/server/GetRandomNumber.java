package server;

import Hello.IGetRandomNumer;
import com.zeroc.Ice.Current;

public class GetRandomNumber implements IGetRandomNumer {
    @Override
    public int getRandomInt(Current current) {
        return 0;
    }

    @Override
    public double getRandomDouble(Current current) {
        return 0;
    }
}
