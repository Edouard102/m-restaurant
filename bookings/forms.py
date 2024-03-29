from django import forms
from .models import Booking, Table

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer_name', 'booking_date', 'booking_time', 'party_size']

    def clean(self):
        cleaned_data = super().clean()
        booking_date = cleaned_data.get("booking_date")
        booking_time = cleaned_data.get("booking_time")
        if booking_date and booking_time:
            pass