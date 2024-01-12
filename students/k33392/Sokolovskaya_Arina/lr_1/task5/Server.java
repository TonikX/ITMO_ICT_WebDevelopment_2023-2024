package lab1.task5;

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.*;

public class Server {

    private static Map<String, List<Integer>> grades = new HashMap<>();

    static Map<String, List<Integer>> getGrades() {
        return grades;
    }

    public static void main(String[] args) {
        int port = 8080;
        try {
            ServerSocket serverSocket = new ServerSocket(port);
            System.out.println("Server started on port " + port);
            RequestHandler handler = new RequestHandler();
            while (true) {
                Socket clientSocket = serverSocket.accept();
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
