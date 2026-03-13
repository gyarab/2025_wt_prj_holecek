from django.contrib import admin
from django.urls import path
<<<<<<< HEAD

=======
>>>>>>> 98003622fd168199cd758da37475b90883784a3b
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', views.render_aboutabout, name='home'),
    path('about/', views.render_about, name='about'),
]
=======
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('add-review/<int:pk>/', views.add_review, name='add_review'),
]
>>>>>>> 98003622fd168199cd758da37475b90883784a3b
