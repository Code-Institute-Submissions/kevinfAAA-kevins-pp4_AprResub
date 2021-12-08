from django.contrib import admin
from .models import Reservations
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Reservations)
class ReservationsAdmin(SummernoteModelAdmin):

    summernote_fields = ('comments')
