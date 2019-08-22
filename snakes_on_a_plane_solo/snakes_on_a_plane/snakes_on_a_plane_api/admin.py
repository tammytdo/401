from django.contrib import admin
from .models import Flight, Seat, Passenger

# Register your models here.
admin.site.register(Flight)
admin.site.register(Seat)
admin.site.register(Passenger)