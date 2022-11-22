from django.shortcuts import render
from .models import DestCommonInfo, Destination
# Create your views here.
def index(request):
    destinations = DestCommonInfo.objects.all()
    context={
        'title' : 'List of destinations',
        'destinations' : destinations
    }
    return render(request, 'pages/destination_list.html', context)

def destination_detail(request, slug):
    destination = DestCommonInfo.objects.get(slug__exact=slug)

    context = {
        'destination': destination
    }

    return render(request, 'pages/destination_detail.html', context)