from . import views
from django.urls import path
from .views import BookingsList, BookingsDetail, BookingsCreate, BookingsUpdate, DeleteView


urlpatterns = [  
    path('', views.index, name='home'),
    path('menu/', views.menu, name='menu'),
    path('reservations/', views.reservations, name='reservations'),
    path('bookings/', BookingsList.as_view(), name='bookings'),
    path('reserved/', views.reserved, name='revserved'),
    path('bookings/<int:pk>/', BookingsDetail.as_view(), name='bookings'),
    path('bookings/create/', BookingsCreate.as_view(), name='create'),
    path('bookings/update/<int:pk>/', BookingsUpdate.as_view(), name='update'),
    path('bookings/delete/<int:pk>/', DeleteView.as_view(), name='delete'),
]