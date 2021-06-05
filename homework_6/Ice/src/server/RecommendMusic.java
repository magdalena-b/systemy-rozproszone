package server;

import Hello.IRecommendMusic;
import com.zeroc.Ice.Current;

import java.io.IOException;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import org.json.*;

public class RecommendMusic implements IRecommendMusic {

    List<String> bands = new ArrayList<String>();

    public RecommendMusic() {
        this.bands.add("New Order");
        this.bands.add("Frank Ocean");
        this.bands.add("Lorde");
        this.bands.add("Pezet");
        this.bands.add("Kate Bush");
        this.bands.add("Lady Gaga");

    }

    @Override
    public String recommendMusic(Current current) {

        Random random = new Random();
        int randomInt = random.nextInt(this.bands.size());
        return bands.get(randomInt);

//        URL url = new URL("https://some-random-api.ml/facts/panda");
//        JSONTokener tokener = new JSONTokener(url.openStream());
//        JSONObject obj = new JSONObject(tokener);
//        String fact = obj.getString("fact");
//        return fact;
    }



}
