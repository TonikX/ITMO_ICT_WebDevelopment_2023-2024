## **Задание 5**
Необходимо написать простой web-сервер для обработки GET и POST http
запросов.

**Задание**: сделать сервер, который может:
● Принять и записать информацию о дисциплине и оценке по дисциплине.
● Отдать информацию обо всех оценах по дсициплине в виде html-страницы.



    public class Server {
    
        private static Map<String, List<Integer>> grades = new HashMap<>();
    
        static Map<String, List<Integer>> getGrades() {
            return grades;
        }
    
        public static void main(String[] args) {
            int port = 8080;
            try {
                ServerSocket serverSocket = new ServerSocket(port); // создаем сокет для сервера
                System.out.println("Server started on port " + port);
                RequestHandler handler = new RequestHandler();
                while (true) {
                    Socket clientSocket = serverSocket.accept(); // ждем подключения клиента
                    handler.handle(clientSocket);
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    
        static void addGrade(String discipline, Integer grade) {
            grades.computeIfAbsent(discipline, k -> new LinkedList<>());
            grades.get(discipline).add(grade);
        }
    
    }

    public class RequestHandler {
    
        public void handle(Socket clientSocket) {
            try {
                BufferedReader input = new BufferedReader(new InputStreamReader(new BufferedInputStream(clientSocket.getInputStream()), "UTF-8"));
                PrintWriter output = new PrintWriter(new OutputStreamWriter(clientSocket.getOutputStream(), "UTF-8"), true);
    
                String request = input.readLine(); // считываем запрос
                if (request != null) {
                    if (request.startsWith("GET")) { // если запрос get
                        handleGetRequest(output); // то обрабатываем get запрос
    
                    } else if (request.startsWith("POST")) { // если запрос post
                        int length = 0;
                        while ((request = input.readLine()) != null && !request.isEmpty()) {
                            if (request.startsWith("Content-Length")) { // ищем длину сообщения
                                length = Integer.parseInt(request.split(" ")[1]); 
                            }
                        }
                        char[] data = new char[length];
                        var str = input.read(data); // считываем входные параметры длины length
                        handlePostRequest(String.valueOf(data), output); // обрабатываем post запрос
                    }
                }
                clientSocket.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    
        private String buildMainPage() {
            StringBuilder response = new StringBuilder();
    
            response.append("<html><head><meta charset=\"UTF-8\"></head><body>");
            response.append("<h1>Оценки по дисциплинам:</h1><ul>");
    
            for (var discipline : Server.getGrades().entrySet()) {
                response.append("<li>").append(discipline.getKey()).append(": ").append(discipline.getValue()).append("</li>");
            }
    
            response.append("</ul>");
            response.append("<h2>Добавить оценку</h2>");
            response.append("<form method=\"POST\">\n");
            response.append("Дисциплина: <input type=\"text\" name=\"Discipline\"><br>");
            response.append("Оценка: <input type=\"text\" name=\"Grade\"><br>");
            response.append("<input type=\"submit\" value=\"Добавить\">");
            response.append("</form>");
            response.append("</body></html>\n");
    
            return response.toString();
        }
    
        private void handleGetRequest(PrintWriter output) {
            String response = buildMainPage(); // собираем страницу
    
            output.println("HTTP/1.1 200 OK");
            output.println("Content-Type: text/html; charset=UTF-8");
            output.println("Content-Length: " + response.getBytes().length);
            output.println(); // пустая строка между заголовками и телом
            output.println(response); // отсылаем
        }
    
        private void handlePostRequest(String line, PrintWriter output) throws IOException {
            Map<String, String> postData = new HashMap<>();
            String[] parts = line.split("&"); // получаем входные параметры
            for (String part : parts) {
                String[] keyValue = part.split("="); // парсим значение каждого параметра
                if (keyValue.length == 2) {
                    String key = URLDecoder.decode(keyValue[0], "UTF-8");
                    String value = URLDecoder.decode(keyValue[1], "UTF-8");
                    postData.put(key, value);
                }
            }
            String discipline = postData.get("Discipline"); // получаем нужные нам параметрыв
            String gradeValue = postData.get("Grade");
    
            if (discipline != null && gradeValue != null) {
                Server.addGrade(discipline, Integer.parseInt(gradeValue)); // добавляем оценку
    
                String response = buildMainPage(); // собираем страницу
    
                output.println("HTTP/1.1 200 OK");
                output.println("Content-Type: text/html; charset=UTF-8");
                output.println("Content-Length: " + response.getBytes().length);
                output.println();
                output.println(response); // отсылаем
            } else { // обрабатываем ошибку
                String response = "Ошибка: Дисциплина и оценка не могут быть null";
    
                output.println("HTTP/1.1 400 Bad Request");
                output.println("Content-Type: text/plain; charset=UTF-8");
                output.println("Content-Length: " + response.getBytes().length);
                output.println();
                output.println(response);
            }
        }
    
    }