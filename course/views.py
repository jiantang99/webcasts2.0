from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    destinations = Destination.objects.all()
    context={
        'title' : 'List of destinations',
        'destinations' : destinations
    }
    return render(request, 'pages/destination_list.html', context)

def destination_detail(request, slug):
    destination = Destination.objects.get(slug__exact=slug)

    context = {
        'destination': destination
    }

    return render(request, 'pages/destination_detail.html', context)