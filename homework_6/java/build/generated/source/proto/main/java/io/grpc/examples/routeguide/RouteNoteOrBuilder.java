// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: route_guide.proto

package io.grpc.examples.routeguide;

public interface RouteNoteOrBuilder extends
    // @@protoc_insertion_point(interface_extends:routeguide.RouteNote)
    com.google.protobuf.MessageOrBuilder {

  /**
   * <pre>
   * The location from which the message is sent.
   * </pre>
   *
   * <code>.routeguide.Point location = 1;</code>
   * @return Whether the location field is set.
   */
  boolean hasLocation();
  /**
   * <pre>
   * The location from which the message is sent.
   * </pre>
   *
   * <code>.routeguide.Point location = 1;</code>
   * @return The location.
   */
  io.grpc.examples.routeguide.Point getLocation();
  /**
   * <pre>
   * The location from which the message is sent.
   * </pre>
   *
   * <code>.routeguide.Point location = 1;</code>
   */
  io.grpc.examples.routeguide.PointOrBuilder getLocationOrBuilder();

  /**
   * <pre>
   * The message to be sent.
   * </pre>
   *
   * <code>string message = 2;</code>
   * @return The message.
   */
  java.lang.String getMessage();
  /**
   * <pre>
   * The message to be sent.
   * </pre>
   *
   * <code>string message = 2;</code>
   * @return The bytes for message.
   */
  com.google.protobuf.ByteString
      getMessageBytes();
}
