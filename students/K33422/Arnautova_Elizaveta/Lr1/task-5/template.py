STARTER = """<!DOCTYPE html>
                        <html lang="ru">"""
HTML_STYLE = """
<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f2f2f2;
        text-align: center;
        padding: 100px;
    }
    h1 {
        color: #333;
    }
    p {
        color: #666;
        font-size: 30px;
    }
</style>
"""

ADD_GRADE = """
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<script>
    function validateGrade() {
        const gradeInput = document.getElementById("grade");
        const gradeValue = parseInt(gradeInput.value);

        if (isNaN(gradeValue) || gradeValue < 1 || gradeValue > 5) {
            alert("Оценка должна быть в диапазоне от 1 до 5");
            return false; 
        }

        return true;
    }
</script>
<body>
    <h2>Введите оценку по предмету</h2>
    <p>
        <form method="POST" action="/" onsubmit="return validateGrade()">
            <input type="text" id="subject" name="subject" placeholder="Предмет">
            <input type="text" id="grade" name="grade" placeholder="Оценка">
            <input type="submit" value="Отправить">
        </form>
    </p>
    <form action="/">
        <input type="submit" value="На главную"/>
    </form>
</body>
"""

NO_PAGE = """
<body>
    <h2>Такой страницы нет :(</h2>
    <form action="/">
        <input type="submit" value="На главную"/>
    </form>
</body>
</html>
"""


YOUR_MARKS = """
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h2>Ваши оценки</h2>
    <table style="border-collapse: collapse; width: 70%;" align="center">
        <tr>
            <th style="border: 1px solid black; padding: 4px;">Предмет</th>
            <th style="border: 1px solid black; padding: 4px;">Оценка</th>
        </tr>
"""

ADDER = """
</table>
<form action="/add_grade" style="padding: 10px;">
    <input type="submit" value="Добавить"/>
</form>
</body>
</html>
"""