## **Задание 3**
Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ
клиент получает http-сообщение, содержащее html-страницу, которую сервер
подгружает из файла index.html.

### Класс сервера ###

    public class Server {
    
        public static void main(String[] args) {
            int port = 8080;
    
            try (ServerSocket serverSocket = new ServerSocket(port)) { // открываем сокет сервера
    
                while (true) {
                    Socket clientSocket = serverSocket.accept(); // ждем подключения
                    handleRequest(clientSocket); // обрабатываем его
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    
        private static void handleRequest(Socket clientSocket) {
            try {
                BufferedReader is = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                OutputStream os = clientSocket.getOutputStream();
    
                String request = is.readLine(); // получаем входящий запрос
                while (request != null && !request.isEmpty()) {
                    System.out.println(request);
                    request = is.readLine();
                }
    
                PrintWriter writer = new PrintWriter(os); 
                writer.println("HTTP/1.1 200 OK"); // отправляем заголовок
                writer.println("Content-Type: text/html; charset=UTF-8");
                writer.println(); // пустая строка между заголоком и телом
                writer.flush();
    
                FileInputStream fileInputStream = new FileInputStream(new File("src/main/java/lab1/task3/index.html"));
                byte[] buffer = new byte[1024];
                int bytesRead;
                while ((bytesRead = fileInputStream.read(buffer)) != -1) {
                    os.write(buffer, 0, bytesRead); // отправляем index.html
                }
                fileInputStream.close();
    
                os.close();
                clientSocket.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    
    }



