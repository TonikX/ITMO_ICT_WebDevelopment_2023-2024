# Вывод оценок

### Представление для вывода оценок:
```python
def register_view(request):
    subjects = Subject.objects.all()
    register = []
    students = User.objects.filter(groups__name='Students')
    for student in students:
        student_marks = []
        for subject in subjects:
            solutions = Solution.objects.filter(student=student, homework__subject=subject)
            subj_marks = []
            for solution in solutions:
                if solution.mark is not None:
                    subj_marks.append(solution.mark)
            student_marks.append((subject, subj_marks))
        register.append((student, student_marks))

    context = {
        'student_data': register,
    }

    return render(request, 'show_marks.html', context)
```


###Шаблон для вывода всех оценок:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Student</title>
</head>
<body>
    <h1>Register</h1>
    {% for student, student_marks in student_data %}
        <h2>{{ student.first_name }}</h2>
        <ul>
            {% for subject, marks in student_marks %}
                <li>
                    {{ subject.name }}:
                    {% if marks %}
                        {% for mark in marks %}
                            {{ mark }}
                        {% endfor %}
                    {% else %}
                        No marks available
                    {% endif %}
                </li>
            {% endfor %}
        </ul>
    {% endfor %}
</body>
</html>
```