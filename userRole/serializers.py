from .models import User,Booking
from rest_framework import serializers,fields

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name','email','password')

class BookingSerializer(serializers.ModelSerializer):
    datetime = fields.DateTimeField(input_formats=['%d-%m-%YT%H:%M:%S'])
    class Meta:
        model = Booking
        fields = '__all__'
