from django.shortcuts import render, redirect
from django.contrib import messages
from home.models import Post, Profil
from .forms import KontaktForm

# Create your views here.
def bilde(request, pk):
    bilde = Post.objects.get(id=pk)
    return render(request, 'showcase.html', {'bilde':bilde})

def home(request):
    posts = Post.objects.all()
    profil = Profil.objects.all()
    return render(request, 'home.html', {'posts':posts, 'profil':profil, 'bilde':bilde})

def kontakt(request):
    form = KontaktForm(auto_id="id_for_%s")
    if request.method == "POST":
        form = KontaktForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Meldingen har blitt sendt.'))
            return redirect('home')
        else:
            messages.success(request, ('Det har skjedd en feil, prøv igjen senere.'))
    else:
        return render(request, 'kontakt.html', {'form':form})