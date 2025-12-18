from django.shortcuts import render
from .models import Musician, Album

def index(request):
    musicians = Musician.objects.all()
    albums = Album.objects.all()
    return render(request, 'main/index.html', {
        'musicians': musicians,
        'albums': albums,
    })

def about_me(request):
    return render(request, 'main/about_me.html')
