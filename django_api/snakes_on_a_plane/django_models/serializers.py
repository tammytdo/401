from rest_framework import serializers
from . import models

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name')
        model = models.Flight

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'seat_num')
        model = models.Seat

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('seat', 'name', 'flight')
        model = models.Passenger