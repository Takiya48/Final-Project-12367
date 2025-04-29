from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking

def home(request):
    bookings = Booking.objects.all()
    return render(request, 'home.html', {'bookings': bookings})

def add_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookingForm()
    return render(request, 'add_booking.html', {'form': form})
