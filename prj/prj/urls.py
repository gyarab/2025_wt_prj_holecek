from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('add-review/<int:pk>/', views.add_review, name='add_review'),
]