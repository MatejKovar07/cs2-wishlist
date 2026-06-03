from django.contrib import admin
from django.urls import path, include
from skins import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.prehled_skinu, name='prehled_skinu'),  # Hlavní stránka poběží hned na základní adrese
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.register, name='register'),
    path('smazat/<int:skin_id>/', views.smazat_skinu, name='smazat_skinu'),
    path('status/<int:skin_id>/', views.zmenit_status, name='zmenit_status'),
]