from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    student_number = models.CharField(max_length=20)
    nationality = models.CharField(max_length=50)
    index_no = models.CharField(max_length=20)  # Ensure this field is included
    validity_start = models.DateField()
    validity_end = models.DateField()
    photo = models.ImageField(upload_to='photos/')
