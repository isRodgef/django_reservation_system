from django.test import TestCase
from reservations.models import Rental, Reservation


# Create your tests here.

class TestRental(TestCase):
    """
        Tests to basic rental functionality
    """

    def setUp(self):
        Rental.objects.create(name='TestRental')

    def test_name(self):
        rental = Rental.objects.all().last()
        self.assertEqual(rental.name, 'TestRental')

class TestReservation(TestCase):
    """
        Tests to reservation functionality
    """

    def setUp(self):
        rental_1 = Rental.objects.create(name="Test1")
        rental_2 = Rental.objects.create(name="Test2")

        Reservation.objects.create(checkin="2011-01-01", checkout="2011-02-01",rental=rental_1)
        Reservation.objects.create(checkin="2011-02-02", checkout="2011-03-02",rental=rental_1)
        Reservation.objects.create(checkin="2011-03-03", checkout="2011-04-03",rental=rental_1)
        Reservation.objects.create(checkin="2011-01-01", checkout="2011-02-01",rental=rental_2)
        Reservation.objects.create(checkin="2011-02-02", checkout="2011-03-02",rental=rental_2)
        Reservation.objects.create(checkin="2011-03-03", checkout="2011-04-03",rental=rental_2)

    def test_rental_name(self):
        reservation = Reservation.objects.first()
        self.assertEqual(reservation.rental.name, "Test1")

        reservation = Reservation.objects.last()
        self.assertEqual(reservation.rental.name, "Test2")
        
    def test_prev_reservations(self):
        reservation = Reservation.objects.last()
        self.assertEqual(reservation.get_prev_reservation_id(), 5)

        reservation = Reservation.objects.first()
        self.assertEqual(reservation.get_prev_reservation_id(), "--")
