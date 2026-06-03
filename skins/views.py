from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from .models import Skin
from .forms import SkinForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registrace proběhla úspěšně! Vítej.")
            return redirect('prehled_skinu')
        else:
            messages.error(request, "Registrace se nezdařila. Zkontroluj zadané údaje.")
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def prehled_skinu(request):
    if request.method == 'POST':
        # Použijeme tvůj formulář a naplníme ho daty z webu
        form = SkinForm(request.POST)
        if form.is_valid():
            skin = form.save(commit=False)
            skin.uzivatel = request.user
            skin.save()
            messages.success(request, "Skin byl úspěšně přidán!")
            return redirect('prehled_skinu')
        else:
            # Pokud zadáš záporné číslo, Django formulář označí jako nevalidní
            # a my tyto chyby vypíšeme uživateli jako červenou hlášku
            for field, errors in form.errors.items():
                for error in errors:
                    # Přeložíme název políčka pro uživatele, aby to vypadalo hezky
                    field_name = "Cena" if field == "purchase_price" else field
                    field_name = "Float" if field == "float_value" else field_name
                    field_name = "Název" if field == "name" else field_name
                    messages.error(request, f"Chyba v poli {field_name}: {error}")
            return redirect('prehled_skinu')

    # Načtení skinů pro přihlášeného uživatele
    skiny = Skin.objects.filter(uzivatel=request.user)
    
    # Vygenerujeme prázdný tvůj formulář pro zobrazení na stránce
    form = SkinForm()
    
    # Výpočty statistik (zde používáme české názvy z tvého models.py)
    celkova_cena = sum(s.cena for s in skiny)
    hodnota_vlastnenych = sum(s.cena for s in skiny if s.koupeno)
    zbyva_doplatit = celkova_cena - hodnota_vlastnenych

    context = {
        'skiny': skiny,
        'form': form, # Posíláme tvůj formulář do šablony
        'celkova_cena': celkova_cena,
        'hodnota_vlastnenych': hodnota_vlastnenych,
        'zbyva_doplatit': zbyva_doplatit,
    }
    return render(request, 'skins/seznam_skinu.html', context)

@login_required
def smazat_skinu(request, skin_id):
    skin = get_object_or_404(Skin, id=skin_id, uzivatel=request.user)
    skin.delete()
    return redirect('prehled_skinu')

@login_required
def zmenit_status(request, skin_id):
    skin = get_object_or_404(Skin, id=skin_id, uzivatel=request.user)
    skin.koupeno = not skin.koupeno
    skin.save()
    return redirect('prehled_skinu')