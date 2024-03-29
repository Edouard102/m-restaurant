from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .models import Booking, Table
from .forms import BookingForm

# Create your views here.

@login_required
def add_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer = request.user
            booking.save()
            messages.success(request, f'Reservation successfully added for {booking.customer_name}.')
            return redirect('booking_detail', pk=booking.pk)
    else:
        form = BookingForm()
    return render(request, 'bookings/add_booking.html', {'form': form})

@login_required
def edit_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reservation successfully deleted.')
            return redirect('booking_detail', pk=pk)
    else:
        form = BookingForm(instance=booking)
    return render(request, 'bookings/edit_booking.html', {'form': form})

@login_required
def delete_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Reservation successfully deleted.')
        return redirect('booking_list')
    return render(request, 'bookings/delete_booking.html', {'booking': booking})

class BookingListView(ListView):
    model = Booking
    template_name = 'bookings/booking_list.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        if self.request.user.is_staff:
            return Booking.objects.all()
        else:
            return Booking.objects.filter(customer=self.request.user)


def is_restaurant_full(date, time):
   
    tables = Table.objects.all()

    reservations = Booking.objects.filter(booking_date=date, booking_time=time)
    
    total_reserved_seats = sum(reservation.party_size for reservation in reservations)
    
    total_capacity = sum(table.table_num_seats for table in tables)
    
    return total_reserved_seats >= total_capacity


date = datetime.today().date()
time = 18  
if is_restaurant_full(date, time):
    print("The restaurant is full.")
else:
    print("There are still available seats.")