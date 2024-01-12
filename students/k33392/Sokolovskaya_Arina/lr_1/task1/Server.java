package lab1.task1;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;

public class Server {

    private static DatagramSocket socket;

    public static void main(String[] args) throws SocketException {
        socket = new DatagramSocket(8080);

        boolean running = true;
        byte[] buf = new byte[1024];
        String message = "hello, user!";

        while (true) {
            DatagramPacket receivedPacket  = new DatagramPacket(buf, buf.length);

            try {
                socket.receive(receivedPacket);
                String received = new String(
                        receivedPacket.getData(), 0, receivedPacket.getLength());
                System.out.println("server received: " + received);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }

            InetAddress address = receivedPacket.getAddress();
            int port = receivedPacket.getPort();
            DatagramPacket packetToSend = new DatagramPacket(message.getBytes(), message.getBytes().length, address, port); // создаем пакет для отправки
            try {
                socket.send(packetToSend);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
    }

}
