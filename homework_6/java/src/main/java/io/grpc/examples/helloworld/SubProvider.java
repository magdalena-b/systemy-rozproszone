package io.grpc.examples.helloworld;

import io.grpc.stub.ServerCallStreamObserver;
import io.grpc.stub.StreamObserver;
import io.grpc.examples.helloworld.SubProviderGrpc.SubProviderImplBase;
import io.grpc.examples.helloworld.HelloWorldProto.*;
import java.util.concurrent.ConcurrentHashMap;


public class SubProvider extends SubProviderImplBase {

    private int counter;
    private final ConcurrentHashMap<String, User> users;

    public SubProvider() {
        
        this.counter = 0;
        this.users = new ConcurrentHashMap<String, User>();
    }

    public boolean addSubscriber(Subscription request) {

        String name = Integer.toString(++counter); 
        // User user = this.users.getOrDefault(userName, null);
        // if (user == null) {
        User user = new User(name);
        // user.subscribe(request);
        this.users.put(name, user);
        // } else {
        //     user.subscribe(request);
        // }

        System.out.println("\n[SUBSCRIBED] New subscription: " + request);
        return true;
    }


    public boolean addListener(String name, ServerCallStreamObserver<NotificationResponse> streamObserver) {
        User userEntry = this.users.getOrDefault(name, null);
        if (userEntry == null) {
            return false;
        }
        // streamObserver.setOnCancelHandler(() -> { // when user disconnects
        //     System.out.println("[INFO] User disconnected. Removing: " + name);
        //     this.users.remove(name);
        // });
        userEntry.setStreamObserver(streamObserver);
        return true;
    }



    @Override
    public void subscribe(Subscription request, StreamObserver<SubscriptionResponse> responseObserver) {
        final SubscriptionResponse.Builder response = SubscriptionResponse.newBuilder();
        responseObserver.onNext(response.build());
        responseObserver.onCompleted();
    }

    @Override
    public void listen(SubscriptionRequest request, StreamObserver<NotificationResponse> responseObserver) {
        // String userName = request.getUserName();
        String name = "1";

        ServerCallStreamObserver<NotificationResponse> properObserver = (ServerCallStreamObserver<NotificationResponse>) responseObserver;
        if (!this.addListener(name, properObserver)) { // checks if such user exists
            responseObserver.onNext(NotificationResponse.newBuilder().build());
            responseObserver.onCompleted();
        }
    }


}