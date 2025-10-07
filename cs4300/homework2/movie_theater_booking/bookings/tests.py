from django.test import TestCase
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking
from datetime import date
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class MovieModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A test movie description",
            release_date=date(2024, 1, 1),
            duration=120
        )
    
    def test_movie_creation(self):
        self.assertEqual(self.movie.title, "Test Movie")
        self.assertEqual(self.movie.duration, 120)
        self.assertIsInstance(self.movie, Movie)
    
    def test_movie_str(self):
        self.assertEqual(str(self.movie), "Test Movie")

class SeatModelTest(TestCase):
    def setUp(self):
        self.seat = Seat.objects.create(seat_number="A1")
    
    def test_seat_creation(self):
        self.assertEqual(self.seat.seat_number, "A1")
        self.assertFalse(self.seat.is_booked)
    
    def test_seat_booking_status(self):
        self.seat.is_booked = True
        self.seat.save()
        self.assertTrue(self.seat.is_booked)
    
    def test_seat_str(self):
        self.assertEqual(str(self.seat), "A1")

class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="Test description",
            release_date=date(2024, 1, 1),
            duration=120
        )
        self.seat = Seat.objects.create(seat_number="A1")
        self.booking = Booking.objects.create(
            movie=self.movie,
            seat=self.seat,
            user=self.user
        )
    
    def test_booking_creation(self):
        self.assertEqual(self.booking.movie, self.movie)
        self.assertEqual(self.booking.seat, self.seat)
        self.assertEqual(self.booking.user, self.user)
    
    def test_booking_unique_constraint(self):
        # Try to create duplicate booking - should fail
        with self.assertRaises(Exception):
            Booking.objects.create(
                movie=self.movie,
                seat=self.seat,
                user=self.user
            )

class MovieAPITest(APITestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="API Test Movie",
            description="Test",
            release_date=date(2024, 1, 1),
            duration=90
        )
    
    def test_get_movie_list(self):
        url = reverse('movie-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_create_movie(self):
        url = reverse('movie-list')
        data = {
            'title': 'New Movie',
            'description': 'New Description',
            'release_date': '2024-06-01',
            'duration': 110
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 2)

class SeatAPITest(APITestCase):
    def setUp(self):
        self.seat = Seat.objects.create(seat_number="B1", is_booked=False)
    
    def test_get_seat_list(self):
        url = reverse('seat-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class BookingAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='apiuser', password='pass')
        self.movie = Movie.objects.create(
            title="Booking Test",
            description="Test",
            release_date=date(2024, 1, 1),
            duration=100
        )
        self.seat = Seat.objects.create(seat_number="C1")
    
    def test_create_booking(self):
        url = reverse('booking-list')
        data = {
            'movie': self.movie.id,
            'seat': self.seat.id,
            'user': self.user.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)