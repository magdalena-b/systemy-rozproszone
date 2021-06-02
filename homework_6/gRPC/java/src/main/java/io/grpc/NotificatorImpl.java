package io.grpc.examples.helloworld;

import io.grpc.stub.ServerCallStreamObserver;
import io.grpc.stub.StreamObserver;


public class NotificatorImpl extends NotificatorGrpc.NotificatorImplBase {

    private SubscriptionHandler subscriptionHandler;

    public NotificatorImpl(SubscriptionHandler subscriptionHandler) {
        this.subscriptionHandler = subscriptionHandler;
    }

    @Override
    public void subscribe(Subscription request, StreamObserver<Notification> responseObserver)
    {
        System.out.println("Client connected");

        ServerCallStreamObserver serverCallresponseObserver = (ServerCallStreamObserver) responseObserver;

        // serverCallresponseObserver.setOnCancelHandler(() -> {
        //     System.out.println("Client disconnected");
        //     this.subscriptionsHandler.removeSubscriber(responseObserver);
        // });

        this.subscriptionHandler.addSubscriber(responseObserver, request);
    }

}