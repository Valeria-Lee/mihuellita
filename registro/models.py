from django.db import models

# Create your models here.
class Usuario(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.username + ' - ' + self.email