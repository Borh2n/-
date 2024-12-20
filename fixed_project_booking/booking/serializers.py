from rest_framework import serializers
from .models import Field, Booking


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
