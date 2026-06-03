from django.contrib import admin
from django.urls import path
from skins import views as skin_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', skin_views.prehled_skinu, name='prehled_skinu'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/register/', skin_views.register, name='register'),
    
    path('smazat/<int:skin_id>/', skin_views.smazat_skinu, name='smazat_skinu'),
    path('status/<int:skin_id>/', skin_views.zmenit_status, name='zmenit_status'),
]