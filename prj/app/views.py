from django.shortcuts import render, get_object_or_404
from .models import KebabShop

def home(request):
    kebabs = KebabShop.objects.all()
    return render(request, 'app/home.html', {'kebabs': kebabs})

def about(request):
    return render(request, 'app/about.html')

def login_view(request):
    return render(request, 'app/login.html')

def profile(request):
    return render(request, 'app/profile.html')

def detail(request, pk):
    kebab = get_object_or_404(KebabShop, pk=pk)
    return render(request, 'app/detail.html', {'kebab': kebab})

def add_review(request, pk):
    return render(request, 'app/add_review.html')

def api_playground(request):
    return render(request, "app/api_playground.html")