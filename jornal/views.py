from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Noticia, Favoritos
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def lista_de_noticias(request):
    noticias = Noticia.objects.all().order_by('-data')
    return render(request, 'index.html', { 'noticias': noticias})

def pagina_noticias(request, slug):
    noticia = Noticia.objects.get(slug=slug)
    return render(request, 'pagina_noticia.html', { 'noticia': noticia})

def index(request):
    query = request.GET.get('q') 
    if query:
        noticias = Noticia.objects.filter(
            Q(titulo__icontains=query) |
            Q(resumo__icontains=query) |
            Q(detalhes__icontains=query)
        ).distinct().order_by('-data')
    else:
        noticias = Noticia.objects.all().order_by('-data')
    contexto = {
        'noticias': noticias,
        'query': query,
    }
    return render(request, 'index.html', contexto)

@login_required
def ver_favoritos(request):
    favoritos_itens = Favoritos.objects.filter(usuario=request.user).order_by('-adicionado')
    noticias_favoritas = [item.noticia for item in favoritos_itens]
    context = {
        'favoritos': noticias_favoritas
    }
    return render(request, 'favoritos.html', context)

@login_required
def add_aos_fav(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    if not Favoritos.objects.filter(usuario=request.user, noticia=noticia).exists():
        Favoritos.objects.create(usuario=request.user, noticia=noticia)
    return redirect('jornal:index')

@login_required
def remover_dos_favoritos(request, noticia_id):
    if request.method == 'POST':
        noticia = get_object_or_404(Noticia, id=noticia_id)
        try:
            favoritos_itens = Favoritos.objects.get(usuario=request.user, noticia=noticia)
            favoritos_itens.delete()
        except Favoritos.DoesNotExist:
            pass  # O item não está na lista, não faz nada

    return redirect('jornal:favoritos')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})
# Create your views here.
