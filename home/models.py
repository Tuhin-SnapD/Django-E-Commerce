from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    phone = models.CharField(max_length=11)
    desc = models.TextField(max_length=650)
    date = models.DateField()

    def __str__(self):
        return self.name