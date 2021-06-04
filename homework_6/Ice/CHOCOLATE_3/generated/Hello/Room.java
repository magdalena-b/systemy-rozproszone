//
// Copyright (c) ZeroC, Inc. All rights reserved.
//
//
// Ice version 3.7.5
//
// <auto-generated>
//
// Generated from file `hello.ice'
//
// Warning: do not edit this file.
//
// </auto-generated>
//

package Hello;

public class Room implements java.lang.Cloneable,
                             java.io.Serializable
{
    public RoomNameIdentifier roomNameId;

    public RoomParameterType parameterType;

    public short parameterValue;

    public Room()
    {
        this.roomNameId = RoomNameIdentifier.MUM;
        this.parameterType = RoomParameterType.TEMPERATURE;
    }

    public Room(RoomNameIdentifier roomNameId, RoomParameterType parameterType, short parameterValue)
    {
        this.roomNameId = roomNameId;
        this.parameterType = parameterType;
        this.parameterValue = parameterValue;
    }

    public boolean equals(java.lang.Object rhs)
    {
        if(this == rhs)
        {
            return true;
        }
        Room r = null;
        if(rhs instanceof Room)
        {
            r = (Room)rhs;
        }

        if(r != null)
        {
            if(this.roomNameId != r.roomNameId)
            {
                if(this.roomNameId == null || r.roomNameId == null || !this.roomNameId.equals(r.roomNameId))
                {
                    return false;
                }
            }
            if(this.parameterType != r.parameterType)
            {
                if(this.parameterType == null || r.parameterType == null || !this.parameterType.equals(r.parameterType))
                {
                    return false;
                }
            }
            if(this.parameterValue != r.parameterValue)
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
        h_ = com.zeroc.IceInternal.HashUtil.hashAdd(h_, "::Hello::Room");
        h_ = com.zeroc.IceInternal.HashUtil.hashAdd(h_, roomNameId);
        h_ = com.zeroc.IceInternal.HashUtil.hashAdd(h_, parameterType);
        h_ = com.zeroc.IceInternal.HashUtil.hashAdd(h_, parameterValue);
        return h_;
    }

    public Room clone()
    {
        Room c = null;
        try
        {
            c = (Room)super.clone();
        }
        catch(CloneNotSupportedException ex)
        {
            assert false; // impossible
        }
        return c;
    }

    public void ice_writeMembers(com.zeroc.Ice.OutputStream ostr)
    {
        RoomNameIdentifier.ice_write(ostr, this.roomNameId);
        RoomParameterType.ice_write(ostr, this.parameterType);
        ostr.writeShort(this.parameterValue);
    }

    public void ice_readMembers(com.zeroc.Ice.InputStream istr)
    {
        this.roomNameId = RoomNameIdentifier.ice_read(istr);
        this.parameterType = RoomParameterType.ice_read(istr);
        this.parameterValue = istr.readShort();
    }

    static public void ice_write(com.zeroc.Ice.OutputStream ostr, Room v)
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

    static public Room ice_read(com.zeroc.Ice.InputStream istr)
    {
        Room v = new Room();
        v.ice_readMembers(istr);
        return v;
    }

    static public void ice_write(com.zeroc.Ice.OutputStream ostr, int tag, java.util.Optional<Room> v)
    {
        if(v != null && v.isPresent())
        {
            ice_write(ostr, tag, v.get());
        }
    }

    static public void ice_write(com.zeroc.Ice.OutputStream ostr, int tag, Room v)
    {
        if(ostr.writeOptional(tag, com.zeroc.Ice.OptionalFormat.FSize))
        {
            int pos = ostr.startSize();
            ice_write(ostr, v);
            ostr.endSize(pos);
        }
    }

    static public java.util.Optional<Room> ice_read(com.zeroc.Ice.InputStream istr, int tag)
    {
        if(istr.readOptional(tag, com.zeroc.Ice.OptionalFormat.FSize))
        {
            istr.skip(4);
            return java.util.Optional.of(Room.ice_read(istr));
        }
        else
        {
            return java.util.Optional.empty();
        }
    }

    private static final Room _nullMarshalValue = new Room();

    /** @hidden */
    public static final long serialVersionUID = -379337273406800841L;
}
