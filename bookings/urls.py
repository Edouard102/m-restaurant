from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_booking, name='add_booking'),
    path('edit/<int:pk>/', views.edit_booking, name='edit_booking'),
    path('delete/<int:pk>/', views.delete_booking, name='delete_booking'),
    path('', views.BookingListView.as_view(), name='booking_list'),
]