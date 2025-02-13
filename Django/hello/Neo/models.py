from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100) # Like varchar of sql
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=20, default='default_password')
    phone = models.CharField(max_length=12)
    desc = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField() #  now run python3 manage.py makemigrations
    
    def __str__(self):
        return self.name