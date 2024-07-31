from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Ride
from .forms import RideForm, UserForm

def home(request):
    return render(request, 'core/home.html')

def ride_list(request):
    rides = Ride.objects.all()
    return render(request, 'core/ride_list.html', {'rides': rides})

def ride_detail(request, pk):
    ride = get_object_or_404(Ride, pk=pk)
    return render(request, 'core/ride_detail.html', {'ride': ride})

@login_required
def ride_create(request):
    if request.method == 'POST':
        form = RideForm(request.POST)
        if form.is_valid():
            ride = form.save(commit=False)
            ride.driver = request.user
            ride.save()
            return redirect('ride_detail', pk=ride.pk)
    else:
        form = RideForm()
    return render(request, 'core/ride_form.html', {'form': form})

@login_required
def user_profile(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = UserForm(instance=request.user)
    return render(request, 'core/user_profile.html', {'form': form})