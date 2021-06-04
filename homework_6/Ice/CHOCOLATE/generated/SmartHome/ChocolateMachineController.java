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

public class ChocolateMachineController extends DrinkController
{
    public ChocolateMachineController()
    {
        super();
    }

    public ChocolateMachineController(DeviceType type, String serialNumber, String name, short minValue, DevicePowerState devicePowerState, short maxTemperature, ChocolateType[] chocolateTypes)
    {
        super(type, serialNumber, name, minValue, devicePowerState, maxTemperature);
        this.chocolateTypes = chocolateTypes;
    }

    public ChocolateType[] chocolateTypes;

    public ChocolateMachineController clone()
    {
        return (ChocolateMachineController)super.clone();
    }

    public static String ice_staticId()
    {
        return "::SmartHome::ChocolateMachineController";
    }

    @Override
    public String ice_id()
    {
        return ice_staticId();
    }

    /** @hidden */
    public static final long serialVersionUID = 5497155779087813346L;

    /** @hidden */
    @Override
    public void _iceWriteImpl(com.zeroc.Ice.OutputStream ostr_)
    {
        ostr_.startSlice(ice_staticId(), -1, false);
        AvailableChocolateTypesHelper.write(ostr_, chocolateTypes);
        ostr_.endSlice();
        super._iceWriteImpl(ostr_);
    }

    /** @hidden */
    @Override
    public void _iceReadImpl(com.zeroc.Ice.InputStream istr_)
    {
        istr_.startSlice();
        chocolateTypes = AvailableChocolateTypesHelper.read(istr_);
        istr_.endSlice();
        super._iceReadImpl(istr_);
    }
}
