from django.shortcuts import render
from home.models import Post, Profil

# Create your views here.
def home(request):
    posts = Post.objects.all()
    profil = Profil.objects.all()
    return render(request, 'home.html', {'posts':posts, 'profil':profil})

def kontakt(request):
    return render(request, 'kontakt.html', {})