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

public class UnknownChocolateType extends com.zeroc.Ice.UserException
{
    public UnknownChocolateType()
    {
    }

    public UnknownChocolateType(Throwable cause)
    {
        super(cause);
    }

    public String ice_id()
    {
        return "::Hello::UnknownChocolateType";
    }

    /** @hidden */
    @Override
    protected void _writeImpl(com.zeroc.Ice.OutputStream ostr_)
    {
        ostr_.startSlice("::Hello::UnknownChocolateType", -1, true);
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
    public static final long serialVersionUID = -3832085336347940639L;
}
