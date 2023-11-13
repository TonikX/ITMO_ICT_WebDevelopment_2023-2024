# Задание №5

???+ question "Задание"

    Необходимо написать простой web-сервер для обработки GET и POST http
    запросов средствами Python и библиотеки socket.

    Базовый класс для простейшей реализации web-сервера доступен по 
    <a href="https://docs.google.com/document/d/1lv_3D9VtMxz8tNkA6rA1xu9zaWEIBGXiLWBo1cse-0k/edit?usp=sharing" 
    class="external-link" target="_blank">ссылке</a>.

    Задание: сделать сервер, который может:

    - Принять и записать информацию о дисциплине и оценке по дисциплине.
    - Отдать информацию обо всех оценах по дсициплине в виде html-страницы.

=== "Сервер"

    ```Python title="server.py"
    --8<-- "lab_1/task5/server.py"
    ```
  
=== "Html"

    ```Html title="index.html"
    --8<-- "lab_1/task5/index.html"
    ```

=== "Html"

    ```Html title="not_found.html"
    --8<-- "lab1/task5/not_found.html"
    ```
