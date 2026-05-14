from django.contrib import admin
from django.urls import path, include
from skins import views as skin_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Přihlášení a odhlášení
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    # Registrace
    path('accounts/register/', skin_views.register, name='register'),
    # Aplikace[cite: 4]
    path('', skin_views.prehled_skinu, name='prehled_skinu'),
    path('smazat/<int:skin_id>/', skin_views.smazat_skin, name='smazat_skin'),
    path('toggle/<int:skin_id>/', skin_views.toggle_owned, name='toggle_owned'),
]