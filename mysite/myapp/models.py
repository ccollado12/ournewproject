from django.db import models
from datetime import datetime

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Faculty(models.Model):
    faculty_name = models.CharField(max_length=40)

class Department(models.Model):
    department_name = models.CharField(max_length=40)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.department_name

class Certificate(models.Model):
    certificate = models.CharField(max_length=40)


class Grade(models.Model):
    type = models.CharField(max_length=40)


class Student(models.Model):
    full_name = models.CharField(max_length=40)
    year_of_graduation = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, default='none')
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    certificate = models.ForeignKey(Certificate, on_delete=models.CASCADE)

    date_of_resumption = models.DateField(default=datetime.today)

    def __str__(self):
        return self.full_name