from django.db import models

# Create your models here.
class Student(models.Model):
    student_id= models.CharField(max_length=200,unique=True) # unique = true ensures no two field in the database has same value for two rows
    first_name= models.CharField(max_length=200)
    last_name= models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    date_of_Birth = models.DateField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F','Female'),
        ('O', 'Other'),
    ]
    address = models.TextField()
    phone=models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"



