from django.db import models

class StudentMarkSheet(models.Model):
    student_name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, unique=True)
    subject1 = models.CharField(max_length=50)
    subject2 = models.CharField(max_length=50)
    subject3 = models.CharField(max_length=50)
    subject4 = models.CharField(max_length=50)
    subject5 = models.CharField(max_length=50)
    score1 = models.DecimalField(max_digits=5, decimal_places=2)
    score2 = models.DecimalField(max_digits=5, decimal_places=2)
    score3 = models.DecimalField(max_digits=5, decimal_places=2)
    score4 = models.DecimalField(max_digits=5, decimal_places=2)
    score5 = models.DecimalField(max_digits=5, decimal_places=2)
    student_passport = models.FileField(upload_to='passports/')

    def __str__(self):
        return self.student_name
