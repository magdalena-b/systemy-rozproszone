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

public class WrongTimeError extends com.zeroc.Ice.UserException
{
    public WrongTimeError()
    {
    }

    public WrongTimeError(Throwable cause)
    {
        super(cause);
    }

    public String ice_id()
    {
        return "::Hello::WrongTimeError";
    }

    /** @hidden */
    @Override
    protected void _writeImpl(com.zeroc.Ice.OutputStream ostr_)
    {
        ostr_.startSlice("::Hello::WrongTimeError", -1, true);
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
    public static final long serialVersionUID = 4408611843798823403L;
}
