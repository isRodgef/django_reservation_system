from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Reservation

# Create your views here.

def index(request):
    reservation_list = Reservation.objects.all()
    template = loader.get_template('reservations.html')
    context = {
        'reservations': reservation_list,
    }
    return HttpResponse(template.render(context, request))