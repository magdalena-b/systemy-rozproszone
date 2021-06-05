package server;

import Hello.ISetTimer;
import Hello.WrongTimeError;
import com.zeroc.Ice.Current;

public class SetTimer implements ISetTimer {
    @Override
    public void setTimer(String time, Current current) throws WrongTimeError {

    }
}
