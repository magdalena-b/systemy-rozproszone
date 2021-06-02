//
// Copyright (c) ZeroC, Inc. All rights reserved.
//

import com.zeroc.demos.Ice.hello.Demo.*;

import java.io.IOException;
import java.net.*;
import java.util.LinkedList;

public class Client
{
    private static String name = "unknown";

    private static LinkedList<Integer> mySensors = new LinkedList<Integer>();
    private static DatagramSocket socket;
    private static InetAddress address;

    static FlushingThread flushingThread;

    public static void initEchoClient() throws SocketException, UnknownHostException {
        socket = new DatagramSocket();
        address = InetAddress.getByName("localhost");
    }

    private static void subscribeToSensors() throws IOException {

        String line = null;
        java.io.BufferedReader in = new java.io.BufferedReader(new java.io.InputStreamReader(System.in));
        do{
            System.out.print("sensor port: ==>");
            System.out.flush();
            line = in.readLine();
            try {
                int port = Integer.parseInt(line);
                mySensors.add(port);
            }catch(Exception e){
                System.out.println("Type number of port or enter");
            }
        }
        while(!line.equals(""));
    }

    public static String callSensor(String msg, int portNumber) throws IOException {
        byte[] buf = new byte[4096];

        DatagramPacket packet
                = new DatagramPacket(buf, buf.length, address, portNumber);
        socket.send(packet);

        packet = new DatagramPacket(buf, buf.length);
        socket.receive(packet);
        String received = new String(
                packet.getData(), 0, packet.getLength());
        return received;
    }

    public static void closeSensorSocket() {
        socket.close();
    }

    public static void main(String[] args) throws IOException, InterruptedException {
        //set name
        String line = null;
        java.io.BufferedReader in = new java.io.BufferedReader(new java.io.InputStreamReader(System.in));

        System.out.print("Client name: ==>");
        System.out.flush();
        line = in.readLine();
        name=line;



        initEchoClient();
        subscribeToSensors();

        int status = 0;
        java.util.List<String> extraArgs = new java.util.ArrayList<>();



        //
        // Try with resources block - communicator is automatically destroyed
        // at the end of this try block
        //
        try(com.zeroc.Ice.Communicator communicator = com.zeroc.Ice.Util.initialize(args, "config.client", extraArgs))
        {
            communicator.getProperties().setProperty("Ice.Default.Package", "com.zeroc.demos.Ice.hello");

            if(!extraArgs.isEmpty())
            {
                System.err.println("too many arguments");
                status = 1;
            }
            else
            {
                status = run(communicator);
            }
        } finally {
            closeSensorSocket();
        }

        System.exit(status);
    }

    private static int run(com.zeroc.Ice.Communicator communicator) throws InterruptedException {
        HelloPrx twoway = HelloPrx.checkedCast(
            communicator.propertyToProxy("Hello.Proxy")).ice_twoway().ice_secure(false);
        if(twoway == null)
        {
            System.err.println("invalid proxy");
            return 1;
        }
        HelloPrx batchOneway = twoway.ice_batchOneway();
        HelloPrx batchDatagram = twoway.ice_batchDatagram();

        flushingThread = new FlushingThread(batchOneway, batchDatagram);
        flushingThread.start();

        menu();

        java.io.BufferedReader in = new java.io.BufferedReader(new java.io.InputStreamReader(System.in));

        String line = null;
        do
        {
            try
            {
                System.out.print("==> ");
                System.out.flush();
                line = in.readLine();
                if(line == null)
                {
                    break;
                }
                else if(line.equals("O"))
                {
                    for (int port : mySensors){
                        String msg = callSensor("", port);
                        System.out.println(msg);
                        batchOneway.sayHello(msg.getBytes());
                    }

                }

                else if(line.equals("D"))
                {
                    for (int port : mySensors){
                        String msg = callSensor("", port);
                        System.out.println(msg);
                        batchDatagram.sayHello(msg.getBytes());
                    }
                }
                else if(line.equals("f"))
                {
                    batchOneway.ice_flushBatchRequests();
                    batchDatagram.ice_flushBatchRequests();
                }

                else if(line.equals("s"))
                {
                    twoway.shutdown();
                }
                else if(line.equals("x"))
                {
                    // Nothing to do
                }
                else if(line.equals("?"))
                {
                    menu();
                }
                else
                {
                    System.out.println("unknown command `" + line + "'");
                    menu();
                }
            }
            catch(java.io.IOException ex)
            {
                ex.printStackTrace();
            }
            catch(com.zeroc.Ice.LocalException ex)
            {
                ex.printStackTrace();
            }
        }
        while(!line.equals("x"));

        flushingThread.join();
        return 0;
    }

    private static void menu()
    {
        System.out.println(
            "usage:\n" +
            "O: send greeting as batch oneway\n" +
            "D: send greeting as batch datagram\n" +
            "f: flush all batch requests (auto-batching per 10s or buffer limit)\n" +
            "s: shutdown server\n" +
            "x: exit\n" +
            "?: help\n");
    }
}

class FlushingThread extends Thread {
    static HelloPrx batchOneway;
    static HelloPrx batchDatagram;
    FlushingThread(HelloPrx batchOneway, HelloPrx batchDatagram){
        this.batchOneway = batchOneway;
        this.batchDatagram = batchDatagram;
    }
    public void run(){
        while (true){
        System.out.println("flush");
            batchOneway.ice_flushBatchRequests();
            batchDatagram.ice_flushBatchRequests();
            try {
                sleep(10000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}