package io.grpc.examples.helloworld;

import io.grpc.stub.ServerCallStreamObserver;
import io.grpc.stub.StreamObserver;
import io.grpc.examples.helloworld.SubProviderGrpc.SubProviderImplBase;
import io.grpc.examples.helloworld.HelloWorldProto.*;


public class SubProvider extends SubProviderImplBase {

    public SubProvider() {
        
    }


    public void subscribe(Subscription request, StreamObserver<SubscriptionResponse> response) {

    }

    public void listen(SubscriptionRequest request, StreamObserver<NotificationResponse> responseObserver) {

    }



}