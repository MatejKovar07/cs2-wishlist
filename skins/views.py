from django.shortcuts import render, redirect, get_object_or_400
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Skin

@login_required
def prehled_skinu(request):
    if request.method == 'POST':
        nazev = request.POST.get('nazev')
        cena_raw = request.POST.get('cena')
        float_raw = request.POST.get('float_value')
        rarita = request.POST.get('rarita')
        
        try:
            cena = float(cena_raw)
            float_value = float(float_raw)
            
            if cena < 0:
                messages.error(request, "Cena nesmí být záporná!")
            elif float_value < 0 or float_value > 1:
                messages.error(request, "Float musí být v rozmezí od 0 do 1!")
            else:
                Skin.objects.create(
                    uzivatel=request.user,
                    nazev=nazev,
                    cena=cena,
                    float_value=float_value,
                    rarita=rarita
                )
                messages.success(request, "Skin byl úspěšně přidán!")
        except ValueError:
            messages.error(request, "Zadány neplatné číselné hodnoty.")
            
        return redirect('prehled_skinu')

    skiny = Skin.objects.filter(uzivatel=request.user)
    
    celkova_cena = sum(s.cena for s in skiny)
    hodnota_vlastnenych = sum(s.cena for s in skiny if s.koupeno)
    zbyva_doplatit = celkova_cena - hodnota_vlastnenych

    context = {
        'skiny': skiny,
        'celkova_cena': celkova_cena,
        'hodnota_vlastnenych': hodnota_vlastnenych,
        'zbyva_doplatit': zbyva_doplatit,
    }
    return render(request, 'skins/seznam_skinu.html', context)

@login_required
def smazat_skinu(request, skin_id):
    skin = get_object_or_400(Skin, id=skin_id, uzivatel=request.user)
    skin.delete()
    return redirect('prehled_skinu')

@login_required
def zmenit_status(request, skin_id):
    skin = get_object_or_400(Skin, id=skin_id, uzivatel=request.user)
    skin.koupeno = not skin.koupeno
    skin.save()
    return redirect('prehled_skinu')