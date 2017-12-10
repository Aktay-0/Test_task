from django.shortcuts import render
from .models import Storage

# Create your views here.

def user_profile(request):
    storage = Storage.objects.get(balance = 5000)
    return render(request, 'task/user_profile.html', {'storage' : storage})
