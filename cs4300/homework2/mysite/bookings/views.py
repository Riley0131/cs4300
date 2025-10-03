from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets

from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

def movie_list(request):
    movies = Movie.objects.all().order_by("title")
    return render(request, "bookings/movie_list.html", {"movies": movies})

def seat_booking(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    seats = movie.seats.order_by("seat_number")
    return render(request, "bookings/seat_booking.html", {"movie": movie, "seats": seats})


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by("title")
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all().order_by("seat_number")
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.select_related("movie", "seat", "user").all().order_by("-booking_date")
    serializer_class = BookingSerializer
