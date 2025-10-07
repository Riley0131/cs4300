from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    
    @action(detail=False, methods=['get'])
    def available(self):
        available_seats = Seat.objects.filter(is_booked=False)
        serializer = self.get_serializer(available_seats, many=True)
        return Response(serializer.data)

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    def get_queryset(self):
        # Filter bookings by user if authenticated
        if self.request.user.is_authenticated:
            return Booking.objects.filter(user=self.request.user)
        return Booking.objects.all()

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

def seat_booking(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    
    if request.method == 'POST':
        seat_id = request.POST.get('seat')
        seat = get_object_or_404(Seat, id=seat_id)
        
        # Check if this exact booking already exists
        existing_booking = Booking.objects.filter(movie=movie, seat=seat).first()
        if existing_booking:
            messages.error(request, f'Seat {seat.seat_number} is already booked for {movie.title}.')
            return redirect('book_seat', movie_id=movie.id)
        
        # Get or create a guest user for bookings
        user, created = User.objects.get_or_create(username='guest')
        
        # Create booking
        Booking.objects.create(
            movie=movie,
            seat=seat,
            user=user
        )
        # Mark seat as booked
        seat.is_booked = True
        seat.save()
        
        messages.success(request, f'Successfully booked seat {seat.seat_number} for {movie.title}!')
        return redirect('booking_history')
    
    # Get seats that haven't been booked for THIS movie
    booked_seat_ids = Booking.objects.filter(movie=movie).values_list('seat_id', flat=True)
    seats = Seat.objects.exclude(id__in=booked_seat_ids)
    
    return render(request, 'bookings/seat_booking.html', {'movie': movie, 'seats': seats})

def booking_history(request):
    # Show all bookings (since we're using guest user)
    bookings = Booking.objects.all().order_by('-booking_date')
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})