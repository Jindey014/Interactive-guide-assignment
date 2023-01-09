from django.shortcuts import render, get_list_or_404
from .models import Places

# Create your views here.


def place_detail(request):
    place = Places.objects.filter(ispopular=True)
    return render(request, 'index.html', {'place': place})

