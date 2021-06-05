package server;

import Hello.IGetAPI;
import Hello.SongNotFoundError;
import com.zeroc.Ice.Current;
import org.json.JSONObject;
import org.json.JSONTokener;


import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;

public class GetAPI implements IGetAPI {

    public GetAPI() {
        System.out.println("Init GetAPI");
    }

    @Override
    public String getPandaFact(Current current) throws IOException {
        URL url = new URL("https://some-random-api.ml/facts/panda");
        JSONTokener tokener = new JSONTokener(url.openStream());
        JSONObject obj = new JSONObject(tokener);
        String fact = obj.getString("fact");
        return fact;
    }

    @Override
    public String getKoalaFact(Current current) throws IOException {
        URL url = new URL("https://some-random-api.ml/facts/koala");
        JSONTokener tokener = new JSONTokener(url.openStream());
        JSONObject obj = new JSONObject(tokener);
        String fact = obj.getString("fact");
        return fact;
    }

    @Override
    public String getLyrics(String title, String artist, Current current) throws SongNotFoundError, IOException {
        String title_formatted = title.toLowerCase().replace(" ", "%20");
        String artist_formatted = artist.toLowerCase();
        String address = "https://some-random-api.ml/lyrics?title=" + title_formatted;
        URL url = new URL(address);
        JSONTokener tokener = new JSONTokener(url.openStream());
        JSONObject obj = new JSONObject(tokener);
        if (obj.getString("author").toLowerCase().equals(artist_formatted)){
            String lyrics = obj.getString("lyrics");
            return lyrics;
        }
        else {
            throw new SongNotFoundError();
        }

    }
}
