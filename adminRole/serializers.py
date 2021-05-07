from rest_framework import serializers
from . import models

class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Advisor
        fields = ('id','name','profile_url')
