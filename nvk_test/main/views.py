from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    inv = TEST_1.objects.all()
    return render(request, 'main/index.html', {'inv': inv})


def repair(request):
    return render(request, 'main/repair.html')


def journal(request):
    return render(request, 'main/journal.html')