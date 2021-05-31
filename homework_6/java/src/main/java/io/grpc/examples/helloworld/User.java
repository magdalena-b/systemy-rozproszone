package io.grpc.examples.helloworld;

import io.grpc.stub.ServerCallStreamObserver;
import io.grpc.stub.StreamObserver;

import io.grpc.examples.helloworld.HelloWorldProto.*;


public class User {

    private ServerCallStreamObserver<NotificationResponse> streamObserver;
    private String name;


    public User(String username) {
        this.streamObserver = null;
        this.name = username;
    }

    public void setStreamObserver(ServerCallStreamObserver<NotificationResponse> streamObserver) {
        
        if (this.streamObserver == null) {
            this.streamObserver = streamObserver;
        }
    }

    public StreamObserver<NotificationResponse> getStreamObserver() {
        return this.streamObserver;
    }




}