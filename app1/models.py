from django.db import models

# Create your models here.


class User(models.Model):
    First_name=models.CharField(max_length=200)
    Last_name=models.CharField(max_length=200)
    Email=models.EmailField(max_length=100,unique=True)

    def __str__(self):
        return self.Email



