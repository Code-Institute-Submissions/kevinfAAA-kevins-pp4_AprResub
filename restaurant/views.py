from django.shortcuts import render
from django.views import generic

def index(request):
        return render(request, 'index.html', {})

def reservations(request):
        return render(request, 'reservations.html', {})
