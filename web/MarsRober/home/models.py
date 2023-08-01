from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    number=models.CharField(max_length=122)
    address=models.CharField(max_length=122)
    
class SignIn(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    address=models.CharField(max_length=122)
    password=models.CharField(max_length=122)

    def __str__(self) :
        return self.name