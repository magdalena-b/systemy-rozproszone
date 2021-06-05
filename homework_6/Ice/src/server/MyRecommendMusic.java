package server;

import Hello.IRecommendMusic;
import com.zeroc.Ice.Current;

import java.io.IOException;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import org.json.*;

public class MyRecommendMusic implements IRecommendMusic {

    List<String> bands = new ArrayList<String>();

    public MyRecommendMusic() {
        this.bands.add("New Order");
        this.bands.add("Frank Ocean");
        this.bands.add("Lorde");
        this.bands.add("Pezet");
        this.bands.add("Kate Bush");
        this.bands.add("Lady Gaga");

    }

    @Override
    public String recommendMusic(Current current) throws IOException {

        Random random = new Random();
        int randomInt = random.nextInt(this.bands.size());
//        return bands.get(randomInt);

        URL url = new URL("https://some-random-api.ml/facts/panda");
        JSONTokener tokener = new JSONTokener(url.openStream());
        JSONObject obj = new JSONObject(tokener);
        String fact = obj.getString("fact");
        return fact;
    }

//    public String getPandaFact(Current current) {
//        String url = "https://some-random-api.ml/facts/panda";
//        JSONObject jsonObject = new JSONObject(url);
//        String fact = (String) jsonObject.getJSONObject(url).get("fact");
//        return fact;
//    }


}
