from django.contrib import admin
from base import models

# Register your models here.
admin.site.register(models.Spaceship)
admin.site.register(models.Spaceport)
admin.site.register(models.Shuttles)
admin.site.register(models.Bookings)
admin.site.register(models.Subscriber)
admin.site.register(models.Transport)