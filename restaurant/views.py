from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from .forms import ReservationsForm
from .models import Reservations
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



def index(request):
        return render(request, 'index.html', {})

def menu(request):
        return render(request, 'menu.html', {})

def reserved(request):
        return render(request, 'reserved.html', {})

def reservations(request):
        submitted = False
        if request.method == "POST":
                form = ReservationsForm(request.POST)
                if form.is_valid():
                        form.save()
                        return HttpResponseRedirect('/reserved?submitted=True')
        else:
                form = ReservationsForm
                if 'submitted' in request.GET:
                        submitted = True
        return render(request, 'reservations.html', {'form':form, 'submitted':submitted})

class BookingsList(ListView):
        model = Reservations
        context_object_name = 'bookings'
        template_name = 'restaurant/bookings_list.html'

        # def get_context_data(self, **kwargs):
        #         context = super().get_context_data(**kwargs)
        #         context['bookings'] = context['bookings'].filter(user=self.request.user)
        #         return context


class BookingsDetail(DetailView):
        model = Reservations
        context_object_name = 'booking'
        template_name = 'restaurant/bookings_detail.html'


class BookingsCreate(CreateView):
        model = Reservations
        template_name = 'restaurant/bookings_form.html'
        fields = ('title', 'number_of_guests', 'date', 'time', 'comments')
        success_url = reverse_lazy('bookings')

class BookingsUpdate(UpdateView):
        model = Reservations
        template_name = 'restaurant/bookings_form.html'
        fields = ('title', 'number_of_guests', 'date', 'time', 'comments')
        success_url = reverse_lazy('bookings')

class DeleteView(DeleteView):
        model = Reservations
        template_name = 'restaurant/bookings_delete.html'
        context_object_name = 'booking'
        success_url = reverse_lazy('bookings')


