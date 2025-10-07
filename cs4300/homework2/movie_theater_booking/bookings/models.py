from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField(help_text="Duration in minutes")
    
    def __str__(self):
        return self.title

class Seat(models.Model):
    seat_number = models.CharField(max_length=10, unique=True)
    is_booked = models.BooleanField(default=False)
    
    def __str__(self):
        return self.seat_number

class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Make optional
    booking_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('movie', 'seat')
    
    def __str__(self):
        username = self.user.username if self.user else "Guest"
        return f"{username} - {self.movie.title} - {self.seat.seat_number}"