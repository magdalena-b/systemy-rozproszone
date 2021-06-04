//
// Copyright (c) ZeroC, Inc. All rights reserved.
//
//
// Ice version 3.7.3
//
// <auto-generated>
//
// Generated from file `Hello.ice'
//
// Warning: do not edit this file.
//
// </auto-generated>
//

package Hello;

public enum RoomNameIdentifier implements java.io.Serializable
{
    MUM(0),
    DAD(1),
    MONIKA(2),
    JAREK(3),
    KITCHEN(4),
    DININGROOM(5),
    BATHROOM(6),
    BASEMENT(7);

    public int value()
    {
        return _value;
    }

    public static RoomNameIdentifier valueOf(int v)
    {
        switch(v)
        {
        case 0:
            return MUM;
        case 1:
            return DAD;
        case 2:
            return MONIKA;
        case 3:
            return JAREK;
        case 4:
            return KITCHEN;
        case 5:
            return DININGROOM;
        case 6:
            return BATHROOM;
        case 7:
            return BASEMENT;
        }
        return null;
    }

    private RoomNameIdentifier(int v)
    {
        _value = v;
    }

    public void ice_write(com.zeroc.Ice.OutputStream ostr)
    {
        ostr.writeEnum(_value, 7);
    }

    public static void ice_write(com.zeroc.Ice.OutputStream ostr, RoomNameIdentifier v)
    {
        if(v == null)
        {
            ostr.writeEnum(Hello.RoomNameIdentifier.MUM.value(), 7);
        }
        else
        {
            ostr.writeEnum(v.value(), 7);
        }
    }

    public static RoomNameIdentifier ice_read(com.zeroc.Ice.InputStream istr)
    {
        int v = istr.readEnum(7);
        return validate(v);
    }

    public static void ice_write(com.zeroc.Ice.OutputStream ostr, int tag, java.util.Optional<RoomNameIdentifier> v)
    {
        if(v != null && v.isPresent())
        {
            ice_write(ostr, tag, v.get());
        }
    }

    public static void ice_write(com.zeroc.Ice.OutputStream ostr, int tag, RoomNameIdentifier v)
    {
        if(ostr.writeOptional(tag, com.zeroc.Ice.OptionalFormat.Size))
        {
            ice_write(ostr, v);
        }
    }

    public static java.util.Optional<RoomNameIdentifier> ice_read(com.zeroc.Ice.InputStream istr, int tag)
    {
        if(istr.readOptional(tag, com.zeroc.Ice.OptionalFormat.Size))
        {
            return java.util.Optional.of(ice_read(istr));
        }
        else
        {
            return java.util.Optional.empty();
        }
    }

    private static RoomNameIdentifier validate(int v)
    {
        final RoomNameIdentifier e = valueOf(v);
        if(e == null)
        {
            throw new com.zeroc.Ice.MarshalException("enumerator value " + v + " is out of range");
        }
        return e;
    }

    private final int _value;
}
