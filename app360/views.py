from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'web/home.html', context)


def dashboard(request):
    return render(request, 'web/dashboard.html', {'title': 'Dashboard'})

def customer(request):
    return render(request, 'web/customer.html', {'title': 'Customer'})

def inquiry(request):
    return render(request, 'web/inquiry.html', {'title': 'Inquiry'})

def alert(request):
    return render(request, 'web/alert.html', {'title': 'Alert'})