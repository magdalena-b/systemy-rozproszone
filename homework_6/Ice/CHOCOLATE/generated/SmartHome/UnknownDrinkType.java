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

public class UnknownDrinkType extends com.zeroc.Ice.UserException
{
    public UnknownDrinkType()
    {
    }

    public UnknownDrinkType(Throwable cause)
    {
        super(cause);
    }

    public String ice_id()
    {
        return "::SmartHome::UnknownDrinkType";
    }

    /** @hidden */
    @Override
    protected void _writeImpl(com.zeroc.Ice.OutputStream ostr_)
    {
        ostr_.startSlice("::SmartHome::UnknownDrinkType", -1, true);
        ostr_.endSlice();
    }

    /** @hidden */
    @Override
    protected void _readImpl(com.zeroc.Ice.InputStream istr_)
    {
        istr_.startSlice();
        istr_.endSlice();
    }

    /** @hidden */
    public static final long serialVersionUID = -3299408286799060901L;
}
