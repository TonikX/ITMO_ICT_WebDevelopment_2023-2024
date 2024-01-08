package lab1.task2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class Client {
    private final Socket clientSocket;
    private final PrintWriter os;
    private final BufferedReader is;

    public Client(int port) throws IOException {
        clientSocket = new Socket("localhost", port);
        os = new PrintWriter(clientSocket.getOutputStream(), true);
        is = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
    }

    public void send(String[] args) throws IOException {
        os.println(args[0] + " " + args[1]);
        System.out.println(is.readLine());
    }

    public void stop() throws IOException {
        is.close();
        os.close();
        clientSocket.close();
    }

    public static void main(String[] args) throws IOException {
        Client client = new Client(8080);
        client.send(args);
        client.stop();
    }

}
