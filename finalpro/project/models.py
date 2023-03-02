from django.db import models

# Create your models here.
class Lecture(models.Model):
    lecture=models.CharField(max_length=6, primary_key=True)
    semester=models.CharField(max_length=20, default="INDUSTRIAL TRAINING")

class Lecturer(models.Model):
    lectID=models.CharField(max_length=10, primary_key=True)
    lectName=models.TextField()
    lectIC= models.CharField(max_length=12, default='020328140000')
    lectPass=models.CharField(max_length=10)

class Student(models.Model):
    studID = models.CharField(max_length=12, primary_key=True)
    studName = models.TextField()
    studIC = models.CharField(max_length=12)
    studPass = models.TextField(max_length=10)
    current_class = models.ForeignKey(Lecture, on_delete=models.CASCADE, to_field='lecture', default='DCS 4A')

class Status(models.Model):
    result_status=models.TextField(primary_key=True)

class Result(models.Model):
    r_id = models.ForeignKey(Student, on_delete=models.CASCADE, to_field='studID')
    r_prog = models.TextField(default='DIPLOMA IN COMPUTER SCIENCE')
    r_class = models.ForeignKey(Lecture, on_delete=models.CASCADE, to_field='lecture')
    r_session = models.CharField(max_length=19, default='SESSION 3 2022/2023')
    r_code = models.CharField(max_length=8)
    r_desc = models.TextField()
    r_grade = models.TextField()
    r_kredit = models.TextField()
    r_status = models.ForeignKey(Status, on_delete=models.CASCADE, to_field='result_status', default='EXCELLENT')

