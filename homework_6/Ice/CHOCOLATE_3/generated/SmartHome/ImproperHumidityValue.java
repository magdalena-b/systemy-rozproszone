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

public class ImproperHumidityValue extends com.zeroc.Ice.UserException
{
    public ImproperHumidityValue()
    {
    }

    public ImproperHumidityValue(Throwable cause)
    {
        super(cause);
    }

    public String ice_id()
    {
        return "::Hello::ImproperHumidityValue";
    }

    /** @hidden */
    @Override
    protected void _writeImpl(com.zeroc.Ice.OutputStream ostr_)
    {
        ostr_.startSlice("::Hello::ImproperHumidityValue", -1, true);
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
    public static final long serialVersionUID = 1505487333294336109L;
}
