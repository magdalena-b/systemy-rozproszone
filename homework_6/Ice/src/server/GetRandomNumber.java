package server;

import Hello.IGetRandomNumber;
import Hello.WrongNumberError;
import com.zeroc.Ice.Current;
import java.util.concurrent.ThreadLocalRandom;

public class GetRandomNumber implements IGetRandomNumber {
    @Override
    public int getRandomInt(String min, String max, Current current) throws WrongNumberError {

        int min_number = 0;
        int max_number = 0;

        try {
            min_number = Integer.parseInt(min);
        }
        catch (NumberFormatException e){
            throw new WrongNumberError();
        }

        try {
            max_number = Integer.parseInt(max);
        }
        catch (NumberFormatException e){
            throw new WrongNumberError();
        }

        try {
            int random_int = ThreadLocalRandom.current().nextInt(min_number, max_number + 1);
            return random_int;
        }
        catch (IllegalArgumentException e){
            throw new WrongNumberError();
        }
    }

    @Override
    public double getRandomDouble(String min, String max, Current current) throws WrongNumberError {

        double min_number = 0.0;
        double max_number = 0.0;

        try {
            min_number = Double.parseDouble(min);
        }
        catch (NumberFormatException e) {
            throw new WrongNumberError();
        }

        try {
            max_number = Double.parseDouble(max);
        }
        catch (NumberFormatException e) {
            throw new WrongNumberError();
        }


        try {
            double random_double = ThreadLocalRandom.current().nextDouble(min_number, max_number);
            return random_double;
        }
        catch (IllegalArgumentException e){
            throw new WrongNumberError();
        }

    }
}
