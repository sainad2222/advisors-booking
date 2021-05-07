from django.db import models

# Advisor model
class Advisor(models.Model):
    name = models.CharField(max_length=200)
    profile_url = models.URLField(max_length=250)

    def __repr__(self):
        return f"Advisor({self.id},{self.name},{self.profile_url})"
