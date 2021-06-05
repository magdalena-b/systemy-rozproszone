package server;

import Hello.ISetTimer;
import Hello.WrongNumberError;
import com.zeroc.Ice.Current;
import java.util.concurrent.TimeUnit;

public class SetTimer implements ISetTimer {

    public SetTimer() {
        System.out.println("Init SetTimer");
    }

    @Override
    public String setTimer(String time, Current current) throws WrongNumberError, InterruptedException {

        try {
            int time_to_sleep = Integer.parseInt(time);
            try {
                TimeUnit.SECONDS.sleep(time_to_sleep);
            }
            catch (InterruptedException e){
                System.out.println("Error in timer");
            }

            return "TIME HAS PASSED";
        }
        catch (NumberFormatException e) {
            throw new WrongNumberError();

        }


    }
}
