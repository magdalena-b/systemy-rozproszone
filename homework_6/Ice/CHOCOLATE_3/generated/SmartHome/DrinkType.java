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

public enum DrinkType implements java.io.Serializable
{
    CHOCOLATE(0),
    TEA(1);

    public int value()
    {
        return _value;
    }

    public static DrinkType valueOf(int v)
    {
        switch(v)
        {
        case 0:
            return CHOCOLATE;
        case 1:
            return TEA;
        }
        return null;
    }

    private DrinkType(int v)
    {
        _value = v;
    }

    public void ice_write(com.zeroc.Ice.OutputStream ostr)
    {
        ostr.writeEnum(_value, 1);
    }

    public static void ice_write(com.zeroc.Ice.OutputStream ostr, DrinkType v)
    {
        if(v == null)
        {
            ostr.writeEnum(Hello.DrinkType.CHOCOLATE.value(), 1);
        }
        else
        {
            ostr.writeEnum(v.value(), 1);
        }
    }

    public static DrinkType ice_read(com.zeroc.Ice.InputStream istr)
    {
        int v = istr.readEnum(1);
        return validate(v);
    }

    public static void ice_write(com.zeroc.Ice.OutputStream ostr, int tag, java.util.Optional<DrinkType> v)
    {
        if(v != null && v.isPresent())
        {
            ice_write(ostr, tag, v.get());
        }
    }

    public static void ice_write(com.zeroc.Ice.OutputStream ostr, int tag, DrinkType v)
    {
        if(ostr.writeOptional(tag, com.zeroc.Ice.OptionalFormat.Size))
        {
            ice_write(ostr, v);
        }
    }

    public static java.util.Optional<DrinkType> ice_read(com.zeroc.Ice.InputStream istr, int tag)
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

    private static DrinkType validate(int v)
    {
        final DrinkType e = valueOf(v);
        if(e == null)
        {
            throw new com.zeroc.Ice.MarshalException("enumerator value " + v + " is out of range");
        }
        return e;
    }

    private final int _value;
}
