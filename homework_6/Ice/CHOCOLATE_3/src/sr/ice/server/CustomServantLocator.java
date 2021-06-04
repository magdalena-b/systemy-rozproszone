package sr.ice.server;

import Hello.IRecommendMusic;
import com.zeroc.Ice.Object;
import com.zeroc.Ice.*;

import java.util.HashMap;

public class CustomServantLocator implements ServantLocator {

    HashMap<String, Object> servants;

    public CustomServantLocator() {
        this.servants = new HashMap<String, Object>();
    }


    @Override
    public LocateResult locate(Current current) {
        String name = current.id.name;
        System.out.println("Locating servant for " + name);

        ObjectAdapter adapter = current.adapter;



        switch (name) {

            case "recommendMusic":
                IRecommendMusic musicServant = new MyRecommendMusic();
                adapter.add(musicServant, new Identity(name, ""));
                return new ServantLocator.LocateResult(musicServant, null);

        }
        throw new IllegalStateException();
    }

    @Override
    public void finished(Current current, Object object, java.lang.Object o) {

    }

    @Override
    public void deactivate(String s) {

    }
}