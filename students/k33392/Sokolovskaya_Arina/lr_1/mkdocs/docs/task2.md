## **Задание 2**
Реализовать клиентскую и серверную часть приложения. Клиент запрашивает у
сервера выполнение математической операции, параметры, которые вводятся с
клавиатуры. Сервер обрабатывает полученные данные и возвращает результат
клиенту а. Теорема Пифагора.

**Реализовать с помощью протокола TCP**

В Java для работы с сокетами есть два класса. Это классы Socket и ServerSocket.

ServerSocket – это специальный класс, объекты которого выполняют роль сервера – т.е. могу обслуживать запросы, пришедшие на определенный сокет.

Класс Socket – это фактически Socket-клиент, с помощью него мы можем послать сообщение некоторому сокету и получить ответ.

### Класс сервера ###

    public class Server {
    
        private ServerSocket serverSocket;
        private Socket clientSocket;
        private PrintWriter out;
        private BufferedReader in;
    
        public void start(int port) throws IOException {
            serverSocket = new ServerSocket(port); // создаем сокет для сервера
            clientSocket = serverSocket.accept(); // ждем подключения
    
            out = new PrintWriter(clientSocket.getOutputStream(), true);
            in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
            String[] args = in.readLine().split(" "); // получаем два числа от юзера, парсим по пробелу
            int a = Integer.parseInt(args[0]);
            int b = Integer.parseInt(args[1]);
            out.println("hypotenuse " + Math.sqrt(a*a +  b*b)); // возвращаем значение гипотенузы
        }
    
        public void stop() throws IOException {
            in.close();
            out.close();
            clientSocket.close();
            serverSocket.close();
        }
    
        public static void main(String[] args) throws IOException {
            Server server = new Server();
            server.start(8080); // запускаем сервер на 8080
            server.stop(); // закрываем Closeble ресурсы
        }
    }
### Класс клиента ###

    public class Client {
        private final PrintWriter os;
        private final BufferedReader is;
        
            public Client(int port) throws IOException {
                clientSocket = new Socket("localhost", port); // создаем сокет клиента
                os = new PrintWriter(clientSocket.getOutputStream(), true);
                is = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
            }
        
            public void send(String[] args) throws IOException {
                os.println(args[0] + " " + args[1]); // отправляем серверу агрументы
                System.out.println(is.readLine()); // получаем ответ от сервера
            }
        
            public void stop() throws IOException {
                is.close();
                os.close();
                clientSocket.close();
            }
        
            public static void main(String[] args) throws IOException {
                Client client = new Client(8080); // подключаемся к порту 8080
                client.send(args); // отправляем серверу аргументы командной строки
                client.stop(); // закрываем Closeble ресурсы
            }
    
    }

 


