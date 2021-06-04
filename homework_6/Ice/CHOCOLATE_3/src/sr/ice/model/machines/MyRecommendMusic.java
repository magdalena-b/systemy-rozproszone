package sr.ice.model.machines;

import Hello.IRecommendMusic;
import com.zeroc.Ice.Current;

public class MyRecommendMusic implements IRecommendMusic {

    @Override
    public String recommendMusic(Current current) {
        return "New Order";
    }
}
