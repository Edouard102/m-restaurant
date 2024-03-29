from django.contrib import admin
from .models import Table, Booking

# Register your models here.

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ("table_number", "table_num_seats")
    list_filter = ("table_num_seats",)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "customer",
        "customer_name",
        "party_size",
        "booking_date",
        "booking_time",
        "table",
        "created_at",
    )
    search_fields = ["id", "customer__username", "customer_name"]
    list_filter = ("booking_date", "booking_time", "table")
