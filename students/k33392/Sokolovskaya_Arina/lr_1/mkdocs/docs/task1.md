## **Задание 1**
Реализовать клиентскую и серверную часть приложения. Клиент отсылает серверу
сообщение «Hello, server». Сообщение должно отразиться на стороне сервера.
Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение должно
отобразиться у клиента.

**Реализовать с помощью протокола UDP**

В Java для работы датаграммами для передачи через UDP используются объекты классов DatagramSocket и DatagramPacket. Для обмена данными отправитель и получатель создают сокеты датаграммного типа — объекты класса DatagramSocket.

### Класс сервера ###

    public class Server {
    
        private static DatagramSocket socket;
    
        public static void main(String[] args) throws SocketException {
            socket = new DatagramSocket(8080); // создаем сокет сервера
    
            boolean running = true;
            byte[] buf = new byte[1024];
            String message = "hello, user!";
    
            while (true) {
                DatagramPacket receivedPacket  = new DatagramPacket(buf, buf.length); // создаем объект для получения пакета
    
                try {
                    socket.receive(receivedPacket); // получаем сообщение от клиента
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
    
                InetAddress address = receivedPacket.getAddress();
                int port = receivedPacket.getPort();
                DatagramPacket packetToSend = new DatagramPacket(message.getBytes(), message.getBytes().length, address, port); // создаем пакет для отправки
                try {
                    socket.send(packetToSend); // отправляем сообщение клиенту
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
        }
    
    }

 

### Класс клиента ###
    
    public class Client {
        private  static DatagramSocket socket;
        private static InetAddress address;
        private  static int port;
    
        public static void main(String[] args) throws IOException {
            socket = new DatagramSocket(); // cоздаем сокет для клиента
            address = InetAddress.getByName("localhost");
            port = 8080;
            String message = "hello, server!";
    
            byte[] buf = message.getBytes();
            DatagramPacket packet = new DatagramPacket(buf, buf.length, address, port);
            socket.send(packet); // отсылаем сообщение серверу
    
            buf = new byte[1024];
            packet = new DatagramPacket(buf, buf.length);
            socket.receive(packet); // получаем сообщение от сервера
    
            socket.close();
        }
    }

