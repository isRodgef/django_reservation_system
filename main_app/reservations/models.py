from django.db import models

# Create your models here.

class Rental(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

class Reservation(models.Model):
    checkin = models.DateField()
    checkout = models.DateField()
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)

    def get_prev_reservation_id(self):
        last_reserved = Reservation.objects.filter(rental=self.rental, id__lt=self.id)
        if last_reserved:
            return last_reserved[len(last_reserved) - 1].id
        return "--"

    class Meta:
        ordering = ["rental_id"]

    