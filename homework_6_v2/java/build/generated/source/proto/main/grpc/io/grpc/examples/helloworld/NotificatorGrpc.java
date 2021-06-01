package io.grpc.examples.helloworld;

import static io.grpc.MethodDescriptor.generateFullMethodName;

/**
 */
@javax.annotation.Generated(
    value = "by gRPC proto compiler (version 1.38.0)",
    comments = "Source: helloworld.proto")
public final class NotificatorGrpc {

  private NotificatorGrpc() {}

  public static final String SERVICE_NAME = "helloworld.Notificator";

  // Static method descriptors that strictly reflect the proto.
  private static volatile io.grpc.MethodDescriptor<io.grpc.examples.helloworld.Subscription,
      io.grpc.examples.helloworld.Notification> getSubscribeMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "subscribe",
      requestType = io.grpc.examples.helloworld.Subscription.class,
      responseType = io.grpc.examples.helloworld.Notification.class,
      methodType = io.grpc.MethodDescriptor.MethodType.SERVER_STREAMING)
  public static io.grpc.MethodDescriptor<io.grpc.examples.helloworld.Subscription,
      io.grpc.examples.helloworld.Notification> getSubscribeMethod() {
    io.grpc.MethodDescriptor<io.grpc.examples.helloworld.Subscription, io.grpc.examples.helloworld.Notification> getSubscribeMethod;
    if ((getSubscribeMethod = NotificatorGrpc.getSubscribeMethod) == null) {
      synchronized (NotificatorGrpc.class) {
        if ((getSubscribeMethod = NotificatorGrpc.getSubscribeMethod) == null) {
          NotificatorGrpc.getSubscribeMethod = getSubscribeMethod =
              io.grpc.MethodDescriptor.<io.grpc.examples.helloworld.Subscription, io.grpc.examples.helloworld.Notification>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.SERVER_STREAMING)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "subscribe"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  io.grpc.examples.helloworld.Subscription.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  io.grpc.examples.helloworld.Notification.getDefaultInstance()))
              .setSchemaDescriptor(new NotificatorMethodDescriptorSupplier("subscribe"))
              .build();
        }
      }
    }
    return getSubscribeMethod;
  }

  /**
   * Creates a new async stub that supports all call types for the service
   */
  public static NotificatorStub newStub(io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<NotificatorStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<NotificatorStub>() {
        @java.lang.Override
        public NotificatorStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new NotificatorStub(channel, callOptions);
        }
      };
    return NotificatorStub.newStub(factory, channel);
  }

  /**
   * Creates a new blocking-style stub that supports unary and streaming output calls on the service
   */
  public static NotificatorBlockingStub newBlockingStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<NotificatorBlockingStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<NotificatorBlockingStub>() {
        @java.lang.Override
        public NotificatorBlockingStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new NotificatorBlockingStub(channel, callOptions);
        }
      };
    return NotificatorBlockingStub.newStub(factory, channel);
  }

  /**
   * Creates a new ListenableFuture-style stub that supports unary calls on the service
   */
  public static NotificatorFutureStub newFutureStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<NotificatorFutureStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<NotificatorFutureStub>() {
        @java.lang.Override
        public NotificatorFutureStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new NotificatorFutureStub(channel, callOptions);
        }
      };
    return NotificatorFutureStub.newStub(factory, channel);
  }

  /**
   */
  public static abstract class NotificatorImplBase implements io.grpc.BindableService {

    /**
     */
    public void subscribe(io.grpc.examples.helloworld.Subscription request,
        io.grpc.stub.StreamObserver<io.grpc.examples.helloworld.Notification> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getSubscribeMethod(), responseObserver);
    }

    @java.lang.Override public final io.grpc.ServerServiceDefinition bindService() {
      return io.grpc.ServerServiceDefinition.builder(getServiceDescriptor())
          .addMethod(
            getSubscribeMethod(),
            io.grpc.stub.ServerCalls.asyncServerStreamingCall(
              new MethodHandlers<
                io.grpc.examples.helloworld.Subscription,
                io.grpc.examples.helloworld.Notification>(
                  this, METHODID_SUBSCRIBE)))
          .build();
    }
  }

  /**
   */
  public static final class NotificatorStub extends io.grpc.stub.AbstractAsyncStub<NotificatorStub> {
    private NotificatorStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected NotificatorStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new NotificatorStub(channel, callOptions);
    }

    /**
     */
    public void subscribe(io.grpc.examples.helloworld.Subscription request,
        io.grpc.stub.StreamObserver<io.grpc.examples.helloworld.Notification> responseObserver) {
      io.grpc.stub.ClientCalls.asyncServerStreamingCall(
          getChannel().newCall(getSubscribeMethod(), getCallOptions()), request, responseObserver);
    }
  }

  /**
   */
  public static final class NotificatorBlockingStub extends io.grpc.stub.AbstractBlockingStub<NotificatorBlockingStub> {
    private NotificatorBlockingStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected NotificatorBlockingStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new NotificatorBlockingStub(channel, callOptions);
    }

    /**
     */
    public java.util.Iterator<io.grpc.examples.helloworld.Notification> subscribe(
        io.grpc.examples.helloworld.Subscription request) {
      return io.grpc.stub.ClientCalls.blockingServerStreamingCall(
          getChannel(), getSubscribeMethod(), getCallOptions(), request);
    }
  }

  /**
   */
  public static final class NotificatorFutureStub extends io.grpc.stub.AbstractFutureStub<NotificatorFutureStub> {
    private NotificatorFutureStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected NotificatorFutureStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new NotificatorFutureStub(channel, callOptions);
    }
  }

  private static final int METHODID_SUBSCRIBE = 0;

  private static final class MethodHandlers<Req, Resp> implements
      io.grpc.stub.ServerCalls.UnaryMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ServerStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ClientStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.BidiStreamingMethod<Req, Resp> {
    private final NotificatorImplBase serviceImpl;
    private final int methodId;

    MethodHandlers(NotificatorImplBase serviceImpl, int methodId) {
      this.serviceImpl = serviceImpl;
      this.methodId = methodId;
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public void invoke(Req request, io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        case METHODID_SUBSCRIBE:
          serviceImpl.subscribe((io.grpc.examples.helloworld.Subscription) request,
              (io.grpc.stub.StreamObserver<io.grpc.examples.helloworld.Notification>) responseObserver);
          break;
        default:
          throw new AssertionError();
      }
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public io.grpc.stub.StreamObserver<Req> invoke(
        io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        default:
          throw new AssertionError();
      }
    }
  }

  private static abstract class NotificatorBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoFileDescriptorSupplier, io.grpc.protobuf.ProtoServiceDescriptorSupplier {
    NotificatorBaseDescriptorSupplier() {}

    @java.lang.Override
    public com.google.protobuf.Descriptors.FileDescriptor getFileDescriptor() {
      return io.grpc.examples.helloworld.HelloWorldProto.getDescriptor();
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.ServiceDescriptor getServiceDescriptor() {
      return getFileDescriptor().findServiceByName("Notificator");
    }
  }

  private static final class NotificatorFileDescriptorSupplier
      extends NotificatorBaseDescriptorSupplier {
    NotificatorFileDescriptorSupplier() {}
  }

  private static final class NotificatorMethodDescriptorSupplier
      extends NotificatorBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoMethodDescriptorSupplier {
    private final String methodName;

    NotificatorMethodDescriptorSupplier(String methodName) {
      this.methodName = methodName;
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.MethodDescriptor getMethodDescriptor() {
      return getServiceDescriptor().findMethodByName(methodName);
    }
  }

  private static volatile io.grpc.ServiceDescriptor serviceDescriptor;

  public static io.grpc.ServiceDescriptor getServiceDescriptor() {
    io.grpc.ServiceDescriptor result = serviceDescriptor;
    if (result == null) {
      synchronized (NotificatorGrpc.class) {
        result = serviceDescriptor;
        if (result == null) {
          serviceDescriptor = result = io.grpc.ServiceDescriptor.newBuilder(SERVICE_NAME)
              .setSchemaDescriptor(new NotificatorFileDescriptorSupplier())
              .addMethod(getSubscribeMethod())
              .build();
        }
      }
    }
    return result;
  }
}
