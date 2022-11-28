from django.db import models

# Create your models here.

class Rental(models.Model):
	name = models.CharField(max_length=100)

class Reservation(models.Model):
    checkin = models.DateField()
    checkout = models.DateField()

    rental_id = models.ForeignKey(Rental, on_delete=models.CASCADE)

    class Meta:
        ordering = ["rental_id"]