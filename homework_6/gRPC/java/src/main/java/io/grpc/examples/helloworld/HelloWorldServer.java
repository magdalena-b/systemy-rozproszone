package io.grpc.examples.helloworld;

import io.grpc.Server;
import io.grpc.ServerBuilder;
import io.grpc.stub.StreamObserver;
import java.io.IOException;
import java.util.concurrent.TimeUnit;
import java.util.logging.Logger;


public class HelloWorldServer {

	private int port = 50051;
	private io.grpc.Server server;

	private SubscriptionHandler subscriptionHandler = new SubscriptionHandler();

	private void start() throws IOException 
	{
      server = ServerBuilder.forPort(port)
          .addService(new NotificatorImpl(this.subscriptionHandler))
          .build()
          .start();

		  System.out.println("Server started, listening on " + port);

		 Runtime.getRuntime().addShutdownHook(new Thread(() -> {
            //  Use stderr here since the logger may have been reset by its JVM shutdown hook.
             System.err.println("*** shutting down gRPC server since JVM is shutting down");
             try {
                 this.stop();
             }
             catch (InterruptedException e){
                 e.printStackTrace();
             }
             
             System.err.println("*** server shut down");
		 }));
	}



  public static void main(String[] args) throws IOException {
      final HelloWorldServer server = new HelloWorldServer();
      server.start();
      server.handleMessages();
  }

    private void stop() throws InterruptedException {
        if (server != null) {
            // server.shutdown().awaitTermination(30, TimeUnit.SECONDS);
            this.subscriptionHandler.shutdown();
            
        }
    }

  public void handleMessages() {

      while (true) {
          this.subscriptionHandler.sendNotification();
          try {
            TimeUnit.SECONDS.sleep(1);
          }
          catch (Exception e) {
              System.out.println(e);
          }
      }

    
  }
}

