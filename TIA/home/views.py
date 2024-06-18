from django.shortcuts import render, redirect
from django.contrib import messages
from home.models import Post, Profil
from .forms import KontaktForm

# Create your views here.
def home(request):
    posts = Post.objects.all()
    profil = Profil.objects.all()
    return render(request, 'home.html', {'posts':posts, 'profil':profil})

def kontakt(request):
    form = KontaktForm
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