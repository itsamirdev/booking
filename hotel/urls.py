from django.urls import path, include
from . import views
# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register('', views.HotelView)

urlpatterns = [
    # path('', include(router.urls)),
    path('reservation/', views.HotelReservation.as_view()),
    path('', views.HotelView.as_view()),
    path('<int:pk>/', views.HotelDetailView.as_view(), name='hotel-detail'),
    path('room/<int:pk>/', views.HotelRoomsView.as_view(), name="rooms-detail"),
    # path('<int:pk>/rooms', views.HotelRoomsView.as_view()),
]

