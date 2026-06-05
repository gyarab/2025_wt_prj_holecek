from django.contrib import admin
from django.urls import path, include
from app import views
from app.api import api as ninja_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('add-review/<int:pk>/', views.add_review, name='add_review'),
    path('api-playground/', views.api_playground, name='api_playground'),
    # API endpoints mounted under /api/
    path('api/', ninja_api.urls),
]