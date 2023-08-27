from django.urls import include, path
from rest_framework import routers
from .views import (
    AirportViewSet,
    FlightViewSet,
    PassengerViewSet,
    ReservationView
)

router = routers.DefaultRouter()
router.register('airports', AirportViewSet)
router.register('flights', FlightViewSet)
router.register('passengers', PassengerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('flights/<int:pk>/reservations', ReservationView.as_view())
]