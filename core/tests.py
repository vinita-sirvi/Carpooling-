from django.test import TestCase
from .models import User, Ride, Location

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass123')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')

class RideModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='driver', email='driver@example.com', password='driverpass123')
        self.departure = Location.objects.create(name='Start', address='Start Address', latitude=0, longitude=0)
        self.destination = Location.objects.create(name='End', address='End Address', latitude=1, longitude=1)

    def test_ride_creation(self):
        ride = Ride.objects.create(
            driver=self.user,
            departure=self.departure,
            destination=self.destination,
            departure_time='2024-01-01 12:00:00',
            available_seats=4,
            price=10.00
        )
        self.assertEqual(ride.driver, self.user)
        self.assertEqual(ride.departure, self.departure)
        self.assertEqual(ride.destination, self.destination)