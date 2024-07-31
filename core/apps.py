from django import forms
from .models import User, Ride

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'profile_picture']

class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['departure', 'destination', 'departure_time', 'available_seats', 'price']