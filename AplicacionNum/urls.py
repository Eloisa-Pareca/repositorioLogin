from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

#from views import viewhello
# #path('', viewhello),

urlpatterns = [
    path('', views.index, name='index'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('home/', views.home, name='home'),
    path('accounts/login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.cerrarsesion, name='cerrar_sesion'),
    path('productos/', login_required(views.productos), name='productos'),
    path('agregar_producto/', views.agregar, name='agregar'),
    path('eliminar/<int:product_id>/', views.eliminar, name='eliminar'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
