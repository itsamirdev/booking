from django.urls import path, include
from . import views
# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register('', views.HotelView)

urlpatterns = [
    # path('', include(router.urls)),
    path('', views.HotelView.as_view(), name='hotel-list'),
    path('<int:pk>/', views.HotelDetailView.as_view(), name='hotel-detail'),
    path('<int:pk>/room', views.HotelRoomsView.as_view(), name='room-detail'),
    path('<int:pk>/reservation', views.HotelReservation.as_view(), name="reservation-detail"),
    # path('<int:pk>/rooms', views.HotelRoomsView.as_view()),
]

