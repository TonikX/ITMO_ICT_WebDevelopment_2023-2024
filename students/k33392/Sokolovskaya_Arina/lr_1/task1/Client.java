package lab1.task1;

import java.io.IOException;
import java.net.*;
import java.util.Arrays;

public class Client {
    private  static DatagramSocket socket;
    private static InetAddress address;
    private  static int port;

    public static void main(String[] args) throws IOException {
        socket = new DatagramSocket();
        address = InetAddress.getByName("localhost");
        port = 8080;
        String message = "hello, server!";

        byte[] buf = message.getBytes();
        DatagramPacket packet = new DatagramPacket(buf, buf.length, address, port);
        socket.send(packet);

        buf = new byte[1024];
        packet = new DatagramPacket(buf, buf.length);
        socket.receive(packet);
        String received = new String(
                packet.getData(), 0, packet.getLength());
        System.out.println("client received: " + received);

        socket.close();
    }
}
