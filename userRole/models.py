from django.db import models
from adminRole.models import Advisor

class User(models.Model):
    name = models.CharField(max_length = 75)
    email = models.EmailField(max_length = 50,unique=True)
    password = models.CharField(max_length = 200)
    advisors = models.ManyToManyField(Advisor)
    def __str__(self):
        return f"User({self.id},{self.name})"

# booking model with one-to-one relations with Advisor and User models
class Booking(models.Model):
    advisor = models.ForeignKey(Advisor,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    datetime = models.DateTimeField()

