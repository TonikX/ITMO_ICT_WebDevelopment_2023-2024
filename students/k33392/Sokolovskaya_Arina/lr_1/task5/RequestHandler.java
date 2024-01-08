package lab1.task5;

import java.io.*;
import java.net.Socket;
import java.net.URLDecoder;
import java.util.HashMap;
import java.util.Map;

public class RequestHandler {

    public void handle(Socket clientSocket) {
        try {
            BufferedReader input = new BufferedReader(new InputStreamReader(new BufferedInputStream(clientSocket.getInputStream()), "UTF-8"));
            PrintWriter output = new PrintWriter(new OutputStreamWriter(clientSocket.getOutputStream(), "UTF-8"), true);

            String request = input.readLine();
            if (request != null) {
                if (request.startsWith("GET")) {
                    handleGetRequest(output);

                } else if (request.startsWith("POST")) {
                    int length = 0;
                    while ((request = input.readLine()) != null && !request.isEmpty()) {
                        if (request.startsWith("Content-Length")) {
                            length = Integer.parseInt(request.split(" ")[1]);
                        }
                    }
                    char[] data = new char[length];
                    var str = input.read(data);
                    handlePostRequest(String.valueOf(data), output);
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
        String response = buildMainPage();

        output.println("HTTP/1.1 200 OK");
        output.println("Content-Type: text/html; charset=UTF-8");
        output.println("Content-Length: " + response.getBytes().length);
        output.println();
        output.println(response);
    }

    private void handlePostRequest(String line, PrintWriter output) throws IOException {
        Map<String, String> postData = new HashMap<>();
        String[] parts = line.split("&");
        for (String part : parts) {
            String[] keyValue = part.split("=");
            if (keyValue.length == 2) {
                String key = URLDecoder.decode(keyValue[0], "UTF-8");
                String value = URLDecoder.decode(keyValue[1], "UTF-8");
                postData.put(key, value);
            }
        }
        String discipline = postData.get("Discipline");
        String gradeValue = postData.get("Grade");

        if (discipline != null && gradeValue != null) {
            Server.addGrade(discipline, Integer.parseInt(gradeValue));

            String response = buildMainPage();

            output.println("HTTP/1.1 200 OK");
            output.println("Content-Type: text/html; charset=UTF-8");
            output.println("Content-Length: " + response.getBytes().length);
            output.println();
            output.println(response);
        } else {
            String response = "Ошибка: Дисциплина и оценка не могут быть null";

            output.println("HTTP/1.1 400 Bad Request");
            output.println("Content-Type: text/plain; charset=UTF-8");
            output.println("Content-Length: " + response.getBytes().length);
            output.println();
            output.println(response);
        }
    }

}
