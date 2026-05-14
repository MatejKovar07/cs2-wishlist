import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Skin
from .forms import SkinForm

def get_market_price(name):
    try:
        url = f"https://v1.skinport.com/api/v1/items?app_id=730&currency=EUR&market_hash_name={name}"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data: return data[0].get('min_price')
    except: return None
    return None

# Nový pohled pro vytvoření účtu
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Automatické přihlášení
            return redirect('prehled_skinu')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def prehled_skinu(request):
    if request.method == "POST":
        form = SkinForm(request.POST)
        if form.is_valid():
            skin = form.save(commit=False)
            skin.user = request.user
            m_price = get_market_price(skin.name)
            skin.current_price = m_price if m_price else skin.purchase_price
            skin.save()
            return redirect('prehled_skinu')
    
    skiny = Skin.objects.filter(user=request.user)
    celkova_cena = skiny.aggregate(Sum('current_price'))['current_price__sum'] or 0
    koupeno_hodnota = skiny.filter(is_owned=True).aggregate(Sum('current_price'))['current_price__sum'] or 0
    zbyva_koupit = celkova_cena - koupeno_hodnota

    return render(request, 'skins/seznam_skinu.html', {
        'skiny': skiny, 'form': SkinForm(),
        'celkova_cena': celkova_cena,
        'koupeno_hodnota': koupeno_hodnota,
        'zbyva_koupit': zbyva_koupit,
    })

@login_required
def toggle_owned(request, skin_id):
    skin = get_object_or_404(Skin, id=skin_id, user=request.user)
    skin.is_owned = not skin.is_owned
    skin.save()
    return redirect('prehled_skinu')

@login_required
def smazat_skin(request, skin_id):
    get_object_or_404(Skin, id=skin_id, user=request.user).delete()
    return redirect('prehled_skinu')