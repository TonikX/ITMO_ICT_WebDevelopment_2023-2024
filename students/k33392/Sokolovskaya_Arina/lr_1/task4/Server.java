package lab1.task4;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.HashMap;

public class Server {

    private ServerSocket server;
    private Socket client = null;
    private DataOutputStream os;
    private DataInputStream is;
    private int port = 8080;
    private HashMap<Socket, String> clientList = new HashMap<>();

    public static void main(String[] args) {
        Server a = new Server();
        a.start();
    }

    private void start() {
        try {
            server = new ServerSocket(port);
            System.out.println("Server started on port " + port);
            while (true) {
                client = server.accept();

                ClientHandler clientHandler = new ClientHandler(client);
                clientHandler.start();
            }
        } catch (Exception e) {
            System.out.println("Something went wrong :(");
        }
    }

    private void deleteUser(Socket client) {
        clientList.remove(client);
    }

    private void addUser(Socket client, String name) {
        clientList.put(client, name);
    }


    class ClientHandler extends Thread {
        public Socket client;
        public DataInputStream is;
        public DataOutputStream os;
        private String clientName;
        public ClientHandler(Socket client) throws IOException {
            this.client = client;
            is = new DataInputStream(client.getInputStream());
            os = new DataOutputStream(client.getOutputStream());
        }

        public void run() {

            try {
                registerUser(client);
                while(client.isConnected()) {
                    String message = is.readUTF();
                    System.out.println("User " + clientName + " send new message: " + message);
                    sendToChat(message);
                }
            } catch (Exception e) {
            } finally {
                try {
                    sendToChat("left chat");
                    System.out.println("User " + clientName + " left chat");
                    deleteUser(client);
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }

        }

        private void registerUser(Socket client) throws IOException {
            clientName = is.readUTF();
            addUser(client, clientName);
            os.writeUTF("Successfully connected");
            sendToChat("connected");
            System.out.println("New user connected! Hello " + clientName + "!");
        }

        private void sendToChat(String message) throws IOException {
            for (var to : clientList.keySet()) {
                if (to == client) continue;
                os = new DataOutputStream(to.getOutputStream());
                os.writeUTF(clientName + ": " + message);
            }
        }

    }
}

