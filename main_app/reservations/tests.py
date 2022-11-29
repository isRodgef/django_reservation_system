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
    fixtures = ['rentals.json']


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
