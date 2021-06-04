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

public class Chocolate implements java.lang.Cloneable,
                                  java.io.Serializable
{
    public Drink drink;

    public ChocolateType chocolateType;

    public Chocolate()
    {
        this.drink = new Drink();
        this.chocolateType = ChocolateType.DARK;
    }

    public Chocolate(Drink drink, ChocolateType chocolateType)
    {
        this.drink = drink;
        this.chocolateType = chocolateType;
    }

    public boolean equals(java.lang.Object rhs)
    {
        if(this == rhs)
        {
            return true;
        }
        Chocolate r = null;
        if(rhs instanceof Chocolate)
        {
            r = (Chocolate)rhs;
        }

        if(r != null)
        {
            if(this.drink != r.drink)
            {
                if(this.drink == null || r.drink == null || !this.drink.equals(r.drink))
                {
                    return false;
                }
            }
            if(this.chocolateType != r.chocolateType)
            {
                if(this.chocolateType == null || r.chocolateType == null || !this.chocolateType.equals(r.chocolateType))
                {
                    return false;
                }
            }

            return true;
        }

        return false;
    }

    public int hashCode()
    {
        int h_ = 5381;
        h_ = com.zeroc.IceInternal.HashUtil.hashAdd(h_, "::Hello::Chocolate");
        h_ = com.zeroc.IceInternal.HashUtil.hashAdd(h_, drink);
        h_ = com.zeroc.IceInternal.HashUtil.hashAdd(h_, chocolateType);
        return h_;
    }

    public Chocolate clone()
    {
        Chocolate c = null;
        try
        {
            c = (Chocolate)super.clone();
        }
        catch(CloneNotSupportedException ex)
        {
            assert false; // impossible
        }
        return c;
    }

    public void ice_writeMembers(com.zeroc.Ice.OutputStream ostr)
    {
        Drink.ice_write(ostr, this.drink);
        ChocolateType.ice_write(ostr, this.chocolateType);
    }

    public void ice_readMembers(com.zeroc.Ice.InputStream istr)
    {
        this.drink = Drink.ice_read(istr);
        this.chocolateType = ChocolateType.ice_read(istr);
    }

    static public void ice_write(com.zeroc.Ice.OutputStream ostr, Chocolate v)
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

    static public Chocolate ice_read(com.zeroc.Ice.InputStream istr)
    {
        Chocolate v = new Chocolate();
        v.ice_readMembers(istr);
        return v;
    }

    static public void ice_write(com.zeroc.Ice.OutputStream ostr, int tag, java.util.Optional<Chocolate> v)
    {
        if(v != null && v.isPresent())
        {
            ice_write(ostr, tag, v.get());
        }
    }

    static public void ice_write(com.zeroc.Ice.OutputStream ostr, int tag, Chocolate v)
    {
        if(ostr.writeOptional(tag, com.zeroc.Ice.OptionalFormat.FSize))
        {
            int pos = ostr.startSize();
            ice_write(ostr, v);
            ostr.endSize(pos);
        }
    }

    static public java.util.Optional<Chocolate> ice_read(com.zeroc.Ice.InputStream istr, int tag)
    {
        if(istr.readOptional(tag, com.zeroc.Ice.OptionalFormat.FSize))
        {
            istr.skip(4);
            return java.util.Optional.of(Chocolate.ice_read(istr));
        }
        else
        {
            return java.util.Optional.empty();
        }
    }

    private static final Chocolate _nullMarshalValue = new Chocolate();

    /** @hidden */
    public static final long serialVersionUID = 7171746975048113631L;
}
