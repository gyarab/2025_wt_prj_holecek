from django.shortcuts import render

def home(request):
    return render(request, 'app/home.html')

def about(request):
    return render(request, 'app/about.html')

def login_view(request):
    return render(request, 'app/login.html')

def profile(request):
    return render(request, 'app/profile.html')

def detail(request, pk):
    return render(request, 'app/detail.html')

def add_review(request, pk):
    return render(request, 'app/add_review.html')