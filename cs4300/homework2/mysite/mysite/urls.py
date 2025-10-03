from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bookings.views import MovieViewSet, SeatViewSet, BookingViewSet, movie_list, seat_booking

router = DefaultRouter()
router.register(r"movies", MovieViewSet)
router.register(r"seats", SeatViewSet)
router.register(r"bookings", BookingViewSet)

urlpatterns = [
    path("", movie_list, name="movie_list"),
    path("movies/<int:pk>/book/", seat_booking, name="book_seat"),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
