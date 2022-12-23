from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def home(request):
    context={
        'title': 'Welcome to best Django Tutorials'
    }
    return render(request, 'pages/home.html', context)


def about_us(request):
    context = {
        'title': 'About us'
    }
    return render(request, 'pages/about_us.html', context)

@login_required
def profile(request):
    user = request.user

    context = {
        'user': user,
    }
    return render(request, 'pages/profile.html', context)