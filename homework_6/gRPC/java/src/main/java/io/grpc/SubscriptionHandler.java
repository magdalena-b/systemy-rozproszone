package io.grpc.examples.helloworld;

import io.grpc.stub.ServerCallStreamObserver;
import io.grpc.stub.StreamObserver;
import java.util.Map;
import java.util.HashMap;
import java.util.concurrent.ThreadLocalRandom;

public class SubscriptionHandler {

    private Map<StreamObserver<Notification>, Subscription> subscribers = new HashMap<>();

    private Map<Integer, String> cities = new HashMap<>();
    private Map<Integer, String> categories = new HashMap<>();


    public SubscriptionHandler(){
        this.cities.put(1, "Krakow");
        this.cities.put(2, "Poznan");
        this.cities.put(3, "Warszawa");

        this.categories.put(1, "Boks");
        this.categories.put(2, "K1");
        this.categories.put(3, "Low_Kick");
        this.categories.put(4, "Kick_Light");
        this.categories.put(5, "Muay_Thai");

    }



    public void addSubscriber(StreamObserver<Notification> responseObserver, Subscription subscription) {
        this.subscribers.put(responseObserver, subscription);
    }

    public void removeSubscriber(StreamObserver<Notification> responseObserver) {
        this.subscribers.remove(responseObserver);
    }

    public void sendNotification() {

        String message;

        int random_city = ThreadLocalRandom.current().nextInt(1, 3 + 1);
        int random_event = ThreadLocalRandom.current().nextInt(1, 3 + 1);
        int random_category = ThreadLocalRandom.current().nextInt(1, 5 + 1);

        String event = "";
        String category = "";
        String city = "";

        if (random_event == 1){
            event = "Mistrzostwa Polski ";
        }
        if (random_event == 2){
            event = "Puchar Polski ";
        }
        if (random_event == 3){
            event = "Amatorska liga ";
        }

        if (random_category == 1){
            category = "w boksie ";
        }
        if (random_category == 2){
            category = "K1 ";
        }
        if (random_category == 3){
            category = "Low Kick ";
        }
        if (random_category == 4){
            category = "Kick Light ";
        }
        if (random_category == 5){
            category = "w Muay Thai ";
        }

        if (random_city == 1){
            city = "w Krakowie";
        }

        if (random_city == 2){
            city = "w Poznaniu";
        }

        if (random_city == 3){
            city = "w Warszawie";
        }

        
        int random_day = ThreadLocalRandom.current().nextInt(1, 30 + 1);
        int random_month = ThreadLocalRandom.current().nextInt(1, 12 + 1);
        int random_year = ThreadLocalRandom.current().nextInt(2022, 2024 + 1);

        message = event + category + city + ", data: " + String.valueOf(random_day)
                    + "." + String.valueOf(random_month) + "." + String.valueOf(random_year);


        Notification notification = Notification.newBuilder()
                .setMessage(message)
                .build();

        System.out.println(message);



        for (Map.Entry<StreamObserver<Notification>, Subscription> entry : this.subscribers.entrySet()){
            if (entry.getValue().getCategoryList().contains(this.categories.get(random_category))
                && entry.getValue().getCityList().contains(this.cities.get(random_city))){
                entry.getKey().onNext(notification);
            }

        }



        // this.subscribers.forEach((StreamObserver<Notification> responseObserver, Subscription subscription) -> {
        //     for (String hashtag : notification.getHashtagsList()) {
        //         if (subscription.getHashtagsList().contains(hashtag)) {
        //             responseObserver.onNext(notification);
        //             break;
        //         }
        //     }
        // });
        // System.out.println("Message published");
    }

     public void shutdown() {
         this.subscribers.keySet().forEach(StreamObserver::onCompleted);
     }




}