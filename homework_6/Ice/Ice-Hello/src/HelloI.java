//
// Copyright (c) ZeroC, Inc. All rights reserved.
//

import com.zeroc.demos.Ice.hello.Demo.*;

public class HelloI implements Hello
{
    public HelloI() {
        byte [] _byteSeq = new byte[ByteSeqSize.value];
    }
    @Override
    public void sayHello( byte[] message, com.zeroc.Ice.Current current)
    {
        System.out.println("Hello World!");
    }

    @Override
    public void shutdown(com.zeroc.Ice.Current current)
    {
        System.out.println("Shutting down...");
        current.adapter.getCommunicator().shutdown();
    }
}
