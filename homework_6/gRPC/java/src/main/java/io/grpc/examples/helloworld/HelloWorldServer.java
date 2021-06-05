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
             // Use stderr here since the logger may have been reset by its JVM shutdown hook.
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
            server.shutdown().awaitTermination(30, TimeUnit.SECONDS);
        }
    }

  public void handleMessages() {
      // logger.info("Waiting for messages...");

      // BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

      while (true) {
            // System.out.print("> ");
            // System.out.flush();

          Notification notification = Notification.newBuilder()
              .setMessage("heyy")
              .build();

          this.subscriptionHandler.sendNotification(notification);
          try {
            TimeUnit.SECONDS.sleep(1);
          }
          catch (Exception e) {
              System.out.println(e);
          }
      }

    // this.subscriptionsHandler.shutdown();
  }
}





// /**
//  * Server that manages startup/shutdown of a {@code Greeter} server.
//  */
// public class HelloWorldServer {
//   private static final Logger logger = Logger.getLogger(HelloWorldServer.class.getName());

//   private Server server;

//   private void start() throws IOException {
//     /* The port on which the server should run */
//     int port = 50051;
//     server = ServerBuilder.forPort(port)
//         .addService(new GreeterImpl())
//         .build()
//         .start();
//     logger.info("The coolest server started, listening on " + port);
//     Runtime.getRuntime().addShutdownHook(new Thread() {
//       @Override
//       public void run() {
//         // Use stderr here since the logger may have been reset by its JVM shutdown hook.
//         System.err.println("*** shutting down gRPC server since JVM is shutting down");
//         try {
//           HelloWorldServer.this.stop();
//         } catch (InterruptedException e) {
//           e.printStackTrace(System.err);
//         }
//         System.err.println("*** server shut down");
//       }
//     });
//   }

//   private void stop() throws InterruptedException {
//     if (server != null) {
//       server.shutdown().awaitTermination(30, TimeUnit.SECONDS);
//     }
//   }

//   /**
//    * Await termination on the main thread since the grpc library uses daemon threads.
//    */
//   private void blockUntilShutdown() throws InterruptedException {
//     if (server != null) {
//       server.awaitTermination();
//     }
//   }

//   /**
//    * Main launches the server from the command line.
//    */
//   public static void main(String[] args) throws IOException, InterruptedException {
//     final HelloWorldServer server = new HelloWorldServer();
//     server.start();
//     server.blockUntilShutdown();
//   }

//   static class GreeterImpl extends GreeterGrpc.GreeterImplBase {

//     @Override
//     public void sayHello(HelloRequest req, StreamObserver<HelloReply> responseObserver) {
//       HelloReply reply = HelloReply.newBuilder().setMessage("Hello " + req.getName()).build();
//       responseObserver.onNext(reply);
//       responseObserver.onCompleted();
//     }

//   }
// }
