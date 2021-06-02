package io.grpc.examples.helloworld;

import io.grpc.stub.ServerCallStreamObserver;
import io.grpc.stub.StreamObserver;
import java.util.Map;
import java.util.HashMap;

public class SubscriptionHandler {

    
    private Map<StreamObserver<Notification>, Subscription> subscribers = new HashMap<>();

    public void addSubscriber(StreamObserver<Notification> responseObserver, Subscription subscription) {
        this.subscribers.put(responseObserver, subscription);
    }

    public void removeSubscriber(StreamObserver<Notification> responseObserver) {
        this.subscribers.remove(responseObserver);
    }

    public void sendNotification(Notification notification) {

        System.out.println("Sending notifications");

        for (Map.Entry<StreamObserver<Notification>, Subscription> entry : this.subscribers.entrySet()){
            // responseObserver = entry.getKey();
            entry.getKey().onNext(notification);
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

    // public void shutdown() {
    //     this.subscribers.keySet().forEach(StreamObserver::onCompleted);
    // }




}