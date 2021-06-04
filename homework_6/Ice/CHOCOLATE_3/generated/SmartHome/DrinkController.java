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

public class DrinkController extends Device
{
    public DrinkController()
    {
        super();
        this.maxTemperature = 100;
    }

    public DrinkController(DeviceType type, String serialNumber, String name, short minValue, DevicePowerState devicePowerState, short maxTemperature)
    {
        super(type, serialNumber, name, minValue, devicePowerState);
        this.maxTemperature = maxTemperature;
    }

    public short maxTemperature;

    public DrinkController clone()
    {
        return (DrinkController)super.clone();
    }

    public static String ice_staticId()
    {
        return "::Hello::DrinkController";
    }

    @Override
    public String ice_id()
    {
        return ice_staticId();
    }

    /** @hidden */
    public static final long serialVersionUID = -1380485224149264848L;

    /** @hidden */
    @Override
    protected void _iceWriteImpl(com.zeroc.Ice.OutputStream ostr_)
    {
        ostr_.startSlice(ice_staticId(), -1, false);
        ostr_.writeShort(maxTemperature);
        ostr_.endSlice();
        super._iceWriteImpl(ostr_);
    }

    /** @hidden */
    @Override
    protected void _iceReadImpl(com.zeroc.Ice.InputStream istr_)
    {
        istr_.startSlice();
        maxTemperature = istr_.readShort();
        istr_.endSlice();
        super._iceReadImpl(istr_);
    }
}
