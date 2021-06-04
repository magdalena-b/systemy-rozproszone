package sr.ice.server;

import Hello.IChocolateMachine;
import Hello.IRoomController;
import Hello.ITeaMachine;
import com.zeroc.Ice.Exception;
import com.zeroc.Ice.Object;
import com.zeroc.Ice.*;
import sr.ice.model.machines.ChocolateMachine;
import sr.ice.model.machines.RoomControllerMachine;
import sr.ice.model.machines.TeaMachine;

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
            case "chocolateMachine":
                IChocolateMachine chocolateServant;
                if (servants.containsKey("chocolateMachine")){
                    chocolateServant = (IChocolateMachine) servants.get("chocolateMachine");
                    System.out.println("Got the old machine");
                }
                else {
                    chocolateServant = new ChocolateMachine("chocolateMachine");
                    adapter.add(chocolateServant, new Identity(name, "machines"));
                    System.out.println("Init chocolate machine");
                }
                return new ServantLocator.LocateResult(chocolateServant, null);

            case "teaMachine":
                ITeaMachine teaServant = new TeaMachine("teaMachine");
                adapter.add(teaServant, new Identity(name, "machines"));
                return new ServantLocator.LocateResult(teaServant, null);
            case "roomControllerMachine":
                IRoomController roomServant = new RoomControllerMachine("roomControllerMachine");
                adapter.add(roomServant, new Identity(name, "machines"));
                return new ServantLocator.LocateResult(roomServant, null);
        }
        throw new RuntimeException();
//        throw new IllegalStateException();
    }

    @Override
    public void finished(Current current, Object object, java.lang.Object o) {

    }

    @Override
    public void deactivate(String s) {

    }
}