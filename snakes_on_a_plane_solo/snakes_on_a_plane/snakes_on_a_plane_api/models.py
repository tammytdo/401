from django.db import models

# Create your models here.
class Flight(models.Model):
    name = models.CharField(max_length=256)
    airborne = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Seat(models.Model):
    seat_num = models.CharField(max_length=3)
    flight = models.ForeignKey('Flight', default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.seat_num

class Passenger(models.Model):
    name = models.CharField(max_length=256)
    seat_num = models.OneToOneField('Seat', default=1, on_delete=models.CASCADE, related_name='passenger')
    flight = models.ForeignKey('Flight', default=1, on_delete=models.CASCADE, related_name='flight')

    def __str__(self):
        return self.name