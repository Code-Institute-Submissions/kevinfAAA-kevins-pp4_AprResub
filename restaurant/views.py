from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from .forms import ReservationsForm

def index(request):
        return render(request, 'index.html', {})

def menu(request):
        return render(request, 'menu.html', {})

def reservations(request):
        submitted = False
        if request.method == "POST":
                form = ReservationsForm(request.POST)
                if form.is_valid():
                        form.save()
                        return HttpResponseRedirect('/?submitted=True')
        else:
                form = ReservationsForm
                if 'submitted' in request.GET:
                        submitted = True
        return render(request, 'reservations.html', {'form':form, 'submitted':submitted})



