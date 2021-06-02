import java.io.IOException;
import java.net.*;
import java.util.Random;

class SubSensor{
    static Random generator = new Random();

    String name;
    String unit;
    boolean inUse;

    SubSensor(String name, String unit) {
        this.name = name;
        this.unit = unit;
        this.inUse = generator.nextBoolean();
    }

    public String getValue(){
        return(generator.nextFloat()*10 + " " + unit + ";");
    }

    public static boolean noneInUse(SubSensor[] array){
        for(SubSensor b : array) if(b.inUse) return false;
        return true;
    }

    public static SubSensor[] getExampleSet(){
        SubSensor subSensors[];
        do {
            subSensors = new SubSensor[]{
                    new SubSensor("distance", "cm"),
                    new SubSensor("water", "mm"),
                    new SubSensor("temp", "C")
            };
        } while (noneInUse(subSensors));
        return subSensors;
    }

    public static String getAllValues(SubSensor[] subSensors){
        String msg = "";
        for (SubSensor ss : subSensors) {
            if (ss.inUse) {
                msg += ss.name + ": " + ss.getValue();
            }
        }
        return msg;
    }

    public static String getAllNames(SubSensor[] subSensors){
        String msg = "";
        for (SubSensor ss : subSensors) {
            if (ss.inUse) {
                msg += ss.name;
                msg += " ";
            }
        }
        return msg;
    }
}


public class Sensor {
    static String owner = "unknown";
    static SubSensor[] subSensors = SubSensor.getExampleSet();

    static int PORT_NUMBER = 12345;

    public static void main (String[] args) throws IOException {

        if (args.length != 2){
            System.out.println("Args [owner] [port]");
            return;
        }
        owner = args[0];
        PORT_NUMBER = Integer.parseInt(args[1]);


        DatagramSocket socket = new DatagramSocket(PORT_NUMBER);
        byte[] buf = new byte[4096];
        boolean running = true;

        System.out.println(Ansi.Black.and(Ansi.BgGreen).colorize("JAVA UDP SENSOR SERVER"));
        System.out.println(Ansi.Green.colorize("I am ready to work, call me " + PORT_NUMBER + "\n"));
        System.out.println(Ansi.Green.colorize("I have "));
        System.out.println(SubSensor.getAllNames(subSensors));
        System.out.println(Ansi.Green.colorize("sensors\n"));

        while (running) {
            DatagramPacket packet
                    = new DatagramPacket(buf, buf.length);
            socket.receive(packet);

            InetAddress address = packet.getAddress();
            int port = packet.getPort();

            String received
                    = new String(packet.getData(), 0, packet.getLength());
            System.out.println(received);
            if (received.equals("end")) {
                running = false;
                continue;
            }
            String msg = SubSensor.getAllValues(subSensors)+"owner: " + owner;
            System.out.println(msg);
            DatagramPacket sensorMsgPacket
                    = new DatagramPacket(msg.getBytes(), msg.getBytes().length, address, port);
            socket.send(sensorMsgPacket);
        }
        socket.close();
    }
}
