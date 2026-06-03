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
            messages.success(request, "Registrace proběhla úspěšně!")
            return redirect('prehled_skinu')
        else:
            messages.error(request, "Registrace se nezdařila.")
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def prehled_skinu(request):
    if request.method == 'POST':
        form = SkinForm(request.POST)
        if form.is_valid():
            # TADY JE TA RYCHLÁ ZÁCHRANA:
            # Vytáhneme data z tvého anglického formuláře
            clean_name = form.cleaned_data.get('name')
            clean_price = form.cleaned_data.get('purchase_price')
            clean_float = form.cleaned_data.get('float_value')
            clean_rarity = form.cleaned_data.get('rarity')

            # Tady provedeme tvrdou kontrolu přímo ve view, aby to neprošlo ani omylem
            if clean_price < 0:
                messages.error(request, "Chyba: Cena nesmí být záporná!")
                return redirect('prehled_skinu')
                
            if clean_float < 0 or clean_float > 1:
                messages.error(request, "Chyba: Float musí být mezi 0.0 a 1.0!")
                return redirect('prehled_skinu')

            # Pokud je vše OK, ručně to naplníme do tvého českého modelu Skin
            Skin.objects.create(
                uzivatel=request.user,
                nazev=clean_name,
                cena=clean_price,
                float_value=clean_float,
                rarita=clean_rarity,
                koupeno=False
            )
            
            messages.success(request, "Skin byl úspěšně přidán!")
            return redirect('prehled_skinu')
        else:
            messages.error(request, "Formulář obsahuje neplatná data.")
            return redirect('prehled_skinu')

    # Načtení dat pro tabulku a statistiky
    skiny = Skin.objects.filter(uzivatel=request.user)
    form = SkinForm()
    
    celkova_cena = sum(s.cena for s in skiny)
    hodnota_vlastnenych = sum(s.cena for s in skiny if s.koupeno)
    zbyva_doplatit = celkova_cena - hodnota_vlastnenych

    context = {
        'skiny': skiny,
        'form': form,
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