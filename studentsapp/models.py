from django.db import models

# Create your models here.
class Student(models.Model):
    roll_no = models.IntegerField(unique=True,primary_key=True)
    name = models.CharField(max_length=100)
    marks = models.FloatField()
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.roll_no} - {self.name}"
