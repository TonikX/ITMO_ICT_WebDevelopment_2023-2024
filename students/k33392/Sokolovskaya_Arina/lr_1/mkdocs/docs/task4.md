## **Задание 4**
Реализовать двухпользовательский или многопользовательский чат. Реализация
многопользовательского часа позволяет получить максимальное количество
баллов.

**Реализовано с помощью протокола TCP**

### Класс сервера ###

    public class Server {
    
        private ServerSocket server;
        private Socket client = null;
        private DataOutputStream os;
        private DataInputStream is;
        private int port = 8080;
        private HashMap<Socket, String> clientList = new HashMap<>();
    
        public static void main(String[] args) {
            Server a = new Server(); // создаем сервер
            a.start();
        }
    
        private void start() {
            try {
                server = new ServerSocket(port); // создаем сокет для сервера
                System.out.println("Server started on port " + port);
                while (true) {
                    client = server.accept(); // ждем подключения пользователя
    
                    ClientHandler clientHandler = new ClientHandler(client);
                    clientHandler.start(); // запускаем поток для обработки пользователя
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
                    while(client.isConnected()) { // пока сокет юзер открыт
                        String message = is.readUTF(); // получаем новое сообщение
                        System.out.println("User " + clientName + " send new message: " + message);
                        sendToChat(message); // отсылаем сообщение в чат
                    }
                } catch (Exception e) {
                } finally {
                    try {
                        sendToChat("left chat");
                        System.out.println("User " + clientName + " left chat");
                        deleteUser(client); // удаляем неактивного юзера
                    } catch (IOException e) {
                        throw new RuntimeException(e);
                    }
                }
    
            }
    
            private void registerUser(Socket client) throws IOException {
                clientName = is.readUTF(); 
                addUser(client, clientName); // добавляем данные нового юзера
                os.writeUTF("Successfully connected");
                sendToChat("connected");
                System.out.println("New user connected! Hello " + clientName + "!");
            }
    
            private void sendToChat(String message) throws IOException {
                for (var to : clientList.keySet()) { // перебираем всех пользователей чата
                    if (to == client) continue; // не отсылаем сообщение самому себе
                    os = new DataOutputStream(to.getOutputStream());
                    os.writeUTF(clientName + ": " + message); // отсылаем сообщение
                }
            }
    
        }
    }

### Класс клиента ###

    public class Client {
    
    
        private final Socket client;
        private final DataOutputStream os;
        private final DataInputStream is;
    
        public Client() throws IOException {
            client = new Socket("localhost", 8080); // создаем сокет для клиента
            os = new DataOutputStream(client.getOutputStream());
            is = new DataInputStream(client.getInputStream());
        }
    
        public static void main(String[] args) throws IOException {
            Client connection = new Client(); // создаем клиента
            connection.start();
    
        }
    
        public void start() throws IOException {
            try {
                BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
                System.out.println("Hello! What is your name?");
                String clientName = in.readLine(); // считываем имя юзера
                os.writeUTF(clientName); // отправляем его серверу для регистрации
    
                String response = is.readUTF(); // получаем ответ от сервера
    
                if (response.equals("Successfully connected")) {
                    System.out.println("Successfully connected, " + clientName + "!");
    
                    // запускаем поток для обработки сообщений от пользователя
                    Thread writer = new Thread(() -> {
                        try {
                            while (true) {
                                String message = in.readLine();
                                os.writeUTF(message);
                            }
                        } catch (Exception e) {}
                    });
    
                    // запускаем поток для обработки сообщений чата
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
 


