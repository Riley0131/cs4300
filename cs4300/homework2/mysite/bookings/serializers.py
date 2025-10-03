from rest_framework import serializers
from .models import Movie, Seat, Booking

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = "__all__"

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
        read_only_fields = ["booking_date"]

    def validate(self, attrs):
        seat = attrs.get("seat")
        movie = attrs.get("movie")
        if seat and movie and getattr(seat, "movie_id", None) != movie.id:
            raise serializers.ValidationError("Seat does not belong to selected movie.")
        if seat and getattr(seat, "is_booked", False):
            raise serializers.ValidationError("Seat is already booked.")
        return attrs

    def create(self, validated_data):
        booking = super().create(validated_data)
        seat = booking.seat
        if hasattr(seat, "is_booked"):
            seat.is_booked = True
            seat.save(update_fields=["is_booked"])
        return booking
