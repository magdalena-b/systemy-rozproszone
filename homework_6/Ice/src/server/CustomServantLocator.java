package server;

import Hello.IGetAPI;
import Hello.IGetRandomNumber;
import Hello.IRecommendMusic;
import Hello.ISetTimer;
import com.zeroc.Ice.Object;
import com.zeroc.Ice.*;

import java.util.HashMap;

public class CustomServantLocator implements ServantLocator {


    @Override
    public LocateResult locate(Current current) {
        String name = current.id.name;
        System.out.println("Locating servant for " + name);

        ObjectAdapter adapter = current.adapter;

        switch (name) {

            case "recommendMusic":
                IRecommendMusic musicServant = new RecommendMusic();
                adapter.add(musicServant, new Identity(name, ""));
                return new ServantLocator.LocateResult(musicServant, null);

            case "getAPI":
                IGetAPI apiServant = new GetAPI();
                adapter.add(apiServant, new Identity(name, ""));
                return new ServantLocator.LocateResult(apiServant, null);

            case "setTimer":
                ISetTimer timerServant = new SetTimer();
                adapter.add(timerServant, new Identity(name, ""));
                return new ServantLocator.LocateResult(timerServant, null);

            case "getRandomNumber":
                IGetRandomNumber randomServant = new GetRandomNumber();
                adapter.add(randomServant, new Identity(name, ""));
                return new ServantLocator.LocateResult(randomServant, null);

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