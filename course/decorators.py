from django.db.models import Q
from django.http import Http404

from course.models import Destination, Company, Booking

def destinations_available(function):
    def wrap(request, *args, **kwargs):
        try:
            Destination.objects.get(Q(slug=kwargs['slug']))
            return function(request, *args, **kwargs)
        except Destination.DoesNotExist:
            raise Http404

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def companies(function):
    def wrap(request, *args, **kwargs):
        try:
            Company.objects.get(Q(slug=kwargs['name']))
            return function(request, *args, **kwargs)
        except Company.DoesNotExist:
            raise Http404

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def bookings(function):
    def wrap(request, *args, **kwargs):
        try:
            Booking.objects.get(Q(slug=kwargs['name']))
            return function(request, *args, **kwargs)
        except Booking.DoesNotExist:
            raise Http404

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

