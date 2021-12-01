from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    inv = Inv.objects.all()
    return render(request, 'main/index.html', {'inv': inv})


def repair(request):
    rep = Rep.objects.all()
    return render(request, 'main/repair.html', {'Rep': rep})


def journal(request):
    return render(request, 'main/journal.html')