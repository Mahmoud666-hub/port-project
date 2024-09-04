from django.db import models
#use Django models


class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    persons = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
