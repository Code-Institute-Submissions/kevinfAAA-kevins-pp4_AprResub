from django import forms
from django.forms import ModelForm
from .models import Reservations


class ReservationsForm(ModelForm):
    class Meta:
        model = Reservations
        fields = ('number_of_guests', 'Date', 'Time', 'comments')