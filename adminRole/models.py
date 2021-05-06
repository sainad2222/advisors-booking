from django.db import models

class Advisor(models.Model):
    name = models.CharField(max_length=200)
    profile_url = models.URLField(max_length=250)

    def __repr__(self):
        return f"Advisor({name},{profile_url})"
