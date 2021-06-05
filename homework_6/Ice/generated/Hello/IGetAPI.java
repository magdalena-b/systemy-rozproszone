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

import java.io.IOException;

public interface IGetAPI extends com.zeroc.Ice.Object
{
    String getPandaFact(com.zeroc.Ice.Current current) throws IOException;

    String getKoalaFact(com.zeroc.Ice.Current current) throws IOException;

    String getLyrics(String title, String artist, com.zeroc.Ice.Current current)
        throws SongNotFoundError, IOException;

    /** @hidden */
    static final String[] _iceIds =
    {
        "::Hello::IGetAPI",
        "::Ice::Object"
    };

    @Override
    default String[] ice_ids(com.zeroc.Ice.Current current)
    {
        return _iceIds;
    }

    @Override
    default String ice_id(com.zeroc.Ice.Current current)
    {
        return ice_staticId();
    }

    static String ice_staticId()
    {
        return "::Hello::IGetAPI";
    }

    /**
     * @hidden
     * @param obj -
     * @param inS -
     * @param current -
     * @return -
    **/
    static java.util.concurrent.CompletionStage<com.zeroc.Ice.OutputStream> _iceD_getPandaFact(IGetAPI obj, final com.zeroc.IceInternal.Incoming inS, com.zeroc.Ice.Current current) throws IOException {
        com.zeroc.Ice.Object._iceCheckMode(null, current.mode);
        inS.readEmptyParams();
        String ret = obj.getPandaFact(current);
        com.zeroc.Ice.OutputStream ostr = inS.startWriteParams();
        ostr.writeString(ret);
        inS.endWriteParams(ostr);
        return inS.setResult(ostr);
    }

    /**
     * @hidden
     * @param obj -
     * @param inS -
     * @param current -
     * @return -
    **/
    static java.util.concurrent.CompletionStage<com.zeroc.Ice.OutputStream> _iceD_getKoalaFact(IGetAPI obj, final com.zeroc.IceInternal.Incoming inS, com.zeroc.Ice.Current current) throws IOException {
        com.zeroc.Ice.Object._iceCheckMode(null, current.mode);
        inS.readEmptyParams();
        String ret = obj.getKoalaFact(current);
        com.zeroc.Ice.OutputStream ostr = inS.startWriteParams();
        ostr.writeString(ret);
        inS.endWriteParams(ostr);
        return inS.setResult(ostr);
    }

    /**
     * @hidden
     * @param obj -
     * @param inS -
     * @param current -
     * @return -
     * @throws com.zeroc.Ice.UserException -
    **/
    static java.util.concurrent.CompletionStage<com.zeroc.Ice.OutputStream> _iceD_getLyrics(IGetAPI obj, final com.zeroc.IceInternal.Incoming inS, com.zeroc.Ice.Current current)
            throws com.zeroc.Ice.UserException, IOException {
        com.zeroc.Ice.Object._iceCheckMode(null, current.mode);
        com.zeroc.Ice.InputStream istr = inS.startReadParams();
        String iceP_title;
        String iceP_artist;
        iceP_title = istr.readString();
        iceP_artist = istr.readString();
        inS.endReadParams();
        String ret = obj.getLyrics(iceP_title, iceP_artist, current);
        com.zeroc.Ice.OutputStream ostr = inS.startWriteParams();
        ostr.writeString(ret);
        inS.endWriteParams(ostr);
        return inS.setResult(ostr);
    }

    /** @hidden */
    final static String[] _iceOps =
    {
        "getKoalaFact",
        "getLyrics",
        "getPandaFact",
        "ice_id",
        "ice_ids",
        "ice_isA",
        "ice_ping"
    };

    /** @hidden */
    @Override
    default java.util.concurrent.CompletionStage<com.zeroc.Ice.OutputStream> _iceDispatch(com.zeroc.IceInternal.Incoming in, com.zeroc.Ice.Current current)
        throws com.zeroc.Ice.UserException
    {
        int pos = java.util.Arrays.binarySearch(_iceOps, current.operation);
        if(pos < 0)
        {
            throw new com.zeroc.Ice.OperationNotExistException(current.id, current.facet, current.operation);
        }

        switch(pos)
        {
            case 0:
            {
                try {
                    return _iceD_getKoalaFact(this, in, current);
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            case 1:
            {
                try {
                    return _iceD_getLyrics(this, in, current);
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            case 2:
            {
                try {
                    return _iceD_getPandaFact(this, in, current);
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            case 3:
            {
                return com.zeroc.Ice.Object._iceD_ice_id(this, in, current);
            }
            case 4:
            {
                return com.zeroc.Ice.Object._iceD_ice_ids(this, in, current);
            }
            case 5:
            {
                return com.zeroc.Ice.Object._iceD_ice_isA(this, in, current);
            }
            case 6:
            {
                return com.zeroc.Ice.Object._iceD_ice_ping(this, in, current);
            }
        }

        assert(false);
        throw new com.zeroc.Ice.OperationNotExistException(current.id, current.facet, current.operation);
    }
}
