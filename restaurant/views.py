from django.shortcuts import render
from django.views import generic
from .forms import ReservationsForm

def index(request):
        return render(request, 'index.html', {})

def menu(request):
        return render(request, 'menu.html', {})

def reservations(request):
        return render(request, 'reservations.html', {})



