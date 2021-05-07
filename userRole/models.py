from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 75)
    email = models.EmailField(max_length = 50,unique=True)
    password = models.CharField(max_length = 200)
    def __str__(self):
        return f"User({self.id},{self.name})"

