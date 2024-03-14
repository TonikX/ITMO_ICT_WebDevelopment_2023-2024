# Код models.py

    from django.db import models

## Teacher
    class Teacher(models.Model):
        first_name = models.CharField(max_length=100)
        last_name = models.CharField(max_length=100)
        room_number = models.IntegerField(null=True)
        subjects = models.ManyToManyField('Subject', through='TeachProcess')
    
        def __str__(self):
            return f'{self.first_name} {self.last_name}'
    
## Grade    
    class Grade(models.Model):
        class GradeTypes(models.IntegerChoices):
            VERY_BAD = 1, "1"
            BAD = 2, "2"
            OK = 3, "3"
            FINE = 4, "4"
            EXCELLENT = 5, "5"
    
        lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)
        student = models.ForeignKey('Student', on_delete=models.CASCADE)
        grade = models.IntegerField(choices=GradeTypes)
    
        def __str__(self):
            return f"{self.lesson}-{self.student} : {self.grade}"
    
## Student    
    class Student(models.Model):
        group = models.ForeignKey('Group', on_delete=models.CASCADE)
        first_name = models.CharField(max_length=100)
        last_name = models.CharField(max_length=100)
        lessons = models.ManyToManyField('Lesson', through='Grade')
    
        def __str__(self):
            return f'{self.first_name} {self.last_name}'
    
## Lesson    
    class Lesson(models.Model):
        teach_process = models.ForeignKey('TeachProcess', on_delete=models.CASCADE)
        group = models.ForeignKey('Group', on_delete=models.CASCADE)
        date = models.DateTimeField()
        students = models.ManyToManyField(Student, through=Grade)
    
        def __str__(self):
            return f"{self.group} - {self.date}"
    
## TeachProcess    
    class TeachProcess(models.Model):
        teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
        subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
        classes = models.ManyToManyField('Group', through=Lesson)
    
        class Meta:
            unique_together = ('teacher', 'subject')
    
        def __str__(self):
            return f"{self.teacher} : {self.subject}"
    
## Group    
    class Group(models.Model):
        group_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
        group_name = models.CharField(max_length=10)
        teachProcess = models.ManyToManyField(TeachProcess, through='Lesson')
    
        def __str__(self):
            return self.group_name
    
## Subject    
    class Subject(models.Model):
        class SubjectType(models.TextChoices):
            MATHEMATICS = 'Математика',
            PHYSICS = 'Физика',
            MUSIC = 'Музыка',
            CHEMISTRY = 'Химия',
            SPORT = 'Спорт',
            ENGLISH = 'Английский',
            RUSSIAN = 'Русский язык'
            LITERATURE = 'Литература'
    
        teachers = models.ManyToManyField(Teacher, through=TeachProcess)
        name = models.CharField(max_length=100, choices=SubjectType)
    
        def __str__(self):
            return self.name
