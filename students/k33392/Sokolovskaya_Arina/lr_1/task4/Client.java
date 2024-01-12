package lab1.task4;

import java.io.*;
import java.net.Socket;

public class Client {


    private final Socket client;
    private final DataOutputStream os;
    private final DataInputStream is;

    public Client() throws IOException {
        client = new Socket("localhost", 8080);
        os = new DataOutputStream(client.getOutputStream());
        is = new DataInputStream(client.getInputStream());
    }

    public static void main(String[] args) throws IOException {
        Client connection = new Client();
        connection.start();

    }

    public void start() throws IOException {
        try {
            BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
            System.out.println("Hello! What is your name?");
            String clientName = in.readLine();
            os.writeUTF(clientName);

            String response = is.readUTF();

            if (response.equals("Successfully connected")) {
                System.out.println("Successfully connected, " + clientName + "!");

                Thread writer = new Thread(() -> {
                    try {
                        while (true) {
                            String message = in.readLine();
                            os.writeUTF(message);
                        }
                    } catch (Exception e) {}
                });

                Thread reader = new Thread(() -> {
                    try {
                        while (true) {
                            String message = is.readUTF();
                            System.out.println(message);
                        }
                    } catch (Exception e) {}
                });

                reader.start();
                writer.start();

                reader.join();
                writer.join();

                client.close();
            } else {
                System.out.println("Something went wrong");
            }
        } catch (Exception e) {
            System.out.println("Something went wrong");
        }
    }

}

