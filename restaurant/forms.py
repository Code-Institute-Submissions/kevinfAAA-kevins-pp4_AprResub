from django import forms
from django.forms import ModelForm
from .models import Reservations


class ReservationsForm(ModelForm):
    class Meta:
        model = Reservations
        fields = ('title', 'number_of_guests', 'date', 'time', 'comments')