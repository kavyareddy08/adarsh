from django.db import models

# Create your models here.
class Register(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.IntegerField()
    state=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)


    def __str__(self):
        return self.fullname
    