package server;

import Hello.IGetAPI;
import Hello.SongNotFoundError;
import com.zeroc.Ice.Current;

public class GetAPI implements IGetAPI {

    @Override
    public String getPandaFact(Current current) {
        return null;
    }

    @Override
    public String getKoalaFact(Current current) {
        return null;
    }

    @Override
    public String getLyrics(String title, Current current) throws SongNotFoundError {
        return null;
    }
}
