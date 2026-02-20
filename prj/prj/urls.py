from django.contrib import admin
from django.urls import path
from app import views  # Import tvých pohledů z aplikace

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),          # Hlavní stránka (KebabTracker)
    path('about/', views.about, name='about'),  # Stránka O projektu
]