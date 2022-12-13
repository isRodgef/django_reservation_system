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

    @staticmethod
    def get_reservations():
        previous_reservation_id = models.Subquery(
            Reservation.objects.filter(
                rental=models.OuterRef("rental"), id__lt=models.OuterRef("id")
            ).order_by("-id").only("id").values("id")[:1]
        )

        reservations = Reservation.objects.select_related('rental').annotate(
            previous_reservation_id=previous_reservation_id
        )
        return reservations

    class Meta:
        ordering = ["rental_id"]

    