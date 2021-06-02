//
// Copyright (c) ZeroC, Inc. All rights reserved.
//

#pragma once

module Demo
{
    sequence<byte> ByteSeq;
    const int ByteSeqSize = 500000;

    interface Hello
    {
        idempotent void sayHello(ByteSeq msg);
        void shutdown();
    }
}
