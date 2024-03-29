from django.db import models
from django.contrib.auth.models import User

# Tables with their capacities
tables_data = [
    (4, 2),  
    (2, 4),  
    (1, 6),
    (1, 8)   
]

class Table(models.Model):
    """Model for a restaurant table"""

    table_number = models.IntegerField(unique=True)
    table_num_seats = models.IntegerField(choices=tables_data, default=2)

    class Meta:
        ordering = ["table_number"]

    def __str__(self):
        return f"Table {self.table_number}"


class Booking(models.Model):
    """Model for restaurant reservations"""

    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bookings", null=True, blank=True
    )
    customer_name = models.CharField(max_length=30)
    party_size = models.IntegerField(default=2)
    booking_date = models.DateField()
    booking_time = models.IntegerField(choices=[(12, '12:00'), (18, '18:00'), (20, '20:00')])
    table = models.ForeignKey(
        'Table', on_delete=models.CASCADE, related_name="bookings"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.CharField(max_length=500, blank=True)
    allergies = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ["booking_date", "booking_time"]

    def __str__(self):
        return f"Booking {self.id} - {self.customer_name}"
