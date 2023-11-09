from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
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
    photo_link = models.URLField()
    class_level = models.IntegerField()

    def total_score(self):
        return self.score1 + self.score2 + self.score3 + self.score4 + self.score5

    def __str__(self):
        return self.name
