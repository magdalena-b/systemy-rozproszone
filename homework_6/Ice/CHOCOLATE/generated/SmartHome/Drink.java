//
// Copyright (c) ZeroC, Inc. All rights reserved.
//
//
// Ice version 3.7.3
//
// <auto-generated>
//
// Generated from file `smarthome.ice'
//
// Warning: do not edit this file.
//
// </auto-generated>
//

package SmartHome;

public class Drink implements java.lang.Cloneable,
                              java.io.Serializable
{
    public short temperature;

    public Drink()
    {
    }

    public Drink(short temperature)
    {
        this.temperature = temperature;
    }

    public boolean equals(java.lang.Object rhs)
    {
        if(this == rhs)
        {
            return true;
        }
        Drink r = null;
        if(rhs instanceof Drink)
        {
            r = (Drink)rhs;
        }

        if(r != null)
        {
            if(this.temperature != r.temperature)
            {
                return false;
            }

            return true;
        }

        return false;
    }

    public int hashCode()
    {
        int h_ = 5381;
        h_ = com.zeroc.IceInternal.HashUtil.hashAdd(h_, "::SmartHome::Drink");
        h_ = com.zeroc.IceInternal.HashUtil.hashAdd(h_, temperature);
        return h_;
    }

    public Drink clone()
    {
        Drink c = null;
        try
        {
            c = (Drink)super.clone();
        }
        catch(CloneNotSupportedException ex)
        {
            assert false; // impossible
        }
        return c;
    }

    public void ice_writeMembers(com.zeroc.Ice.OutputStream ostr)
    {
        ostr.writeShort(this.temperature);
    }

    public void ice_readMembers(com.zeroc.Ice.InputStream istr)
    {
        this.temperature = istr.readShort();
    }

    static public void ice_write(com.zeroc.Ice.OutputStream ostr, Drink v)
    {
        if(v == null)
        {
            _nullMarshalValue.ice_writeMembers(ostr);
        }
        else
        {
            v.ice_writeMembers(ostr);
        }
    }

    static public Drink ice_read(com.zeroc.Ice.InputStream istr)
    {
        Drink v = new Drink();
        v.ice_readMembers(istr);
        return v;
    }

    static public void ice_write(com.zeroc.Ice.OutputStream ostr, int tag, java.util.Optional<Drink> v)
    {
        if(v != null && v.isPresent())
        {
            ice_write(ostr, tag, v.get());
        }
    }

    static public void ice_write(com.zeroc.Ice.OutputStream ostr, int tag, Drink v)
    {
        if(ostr.writeOptional(tag, com.zeroc.Ice.OptionalFormat.VSize))
        {
            ostr.writeSize(2);
            ice_write(ostr, v);
        }
    }

    static public java.util.Optional<Drink> ice_read(com.zeroc.Ice.InputStream istr, int tag)
    {
        if(istr.readOptional(tag, com.zeroc.Ice.OptionalFormat.VSize))
        {
            istr.skipSize();
            return java.util.Optional.of(Drink.ice_read(istr));
        }
        else
        {
            return java.util.Optional.empty();
        }
    }

    private static final Drink _nullMarshalValue = new Drink();

    /** @hidden */
    public static final long serialVersionUID = -9047340142872740628L;
}