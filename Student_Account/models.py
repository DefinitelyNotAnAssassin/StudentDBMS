from email.mime import base
from enum import unique
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models import UniqueConstraint
# Create your models here.

class Account(AbstractUser):
    id_number = models.CharField(max_length=32)
    
    is_student = models.BooleanField(default = False)
    is_teacher = models.BooleanField(default = False)
    is_enrolled = models.BooleanField(default = False)
    is_registrar = models.BooleanField(default = False)
    REQUIRED_FIELDS = ['first_name', 'last_name', 'id_number', 'is_enrolled']
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class TeacherProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, unique=True)
    user.is_teacher = True 
    
    def __str__(self):
        return f"{self.user}"

class Class_Section(models.Model):
    section = models.CharField(max_length=32)
    adviser = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE)
    def __str__(self):
        return self.section


class StudentProfile(models.Model):

    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="student")
    user.is_student = True
    
    section = models.ForeignKey(Class_Section, on_delete=models.CASCADE, related_name="students")
    
    def __str__(self):
        return self.user.username


class Subject(models.Model):
    subject_name = models.CharField(max_length=32)
    teacher = models.ManyToManyField(TeacherProfile, through="SubjectTeacher")

    def __str__(self):
        return self.subject_name

class SubjectTeacher(models.Model):
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    SEMESTER_CHOICES = [("1st", "First Quarter"), ("2nd", 'Second Quarter'), ('3rd', 'Third Quarter'), ('4th', 'Fourth Quarter')]
    semester = models.CharField(choices = SEMESTER_CHOICES, default = "1st", max_length=3)
    students = models.ManyToManyField(StudentProfile, related_name="subjects", through="StudentGrade")
    def __str__(self):
        return f'{self.subject.subject_name}  | {self.teacher.user.first_name}'
    class Meta:
        constraints = [
            UniqueConstraint(fields = ["teacher", "subject", "semester"], name = "Unique Subject Teacher")
        ]

class StudentGrade(models.Model):
    subject_teacher = models.ForeignKey("SubjectTeacher", on_delete=models.CASCADE)
    student = models.ForeignKey('StudentProfile', on_delete=models.CASCADE, related_name="grade")
    grade = models.IntegerField(default=0)

