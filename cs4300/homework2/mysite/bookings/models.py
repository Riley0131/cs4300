from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    release_date = models.DateField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    def __str__(self): return self.title

class Seat(models.Model):
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE, related_name="seats", null=True, blank=True)
    seat_number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)

    class Meta:
        unique_together = ("movie", "seat_number")

class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="bookings")
    seat = models.OneToOneField(Seat, on_delete=models.CASCADE, related_name="booking")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    booking_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        owner = self.user.username if self.user else "guest"
        return f"Booking {self.id} by {owner} for {self.seat}"
