from django.shortcuts import render

def dashboard(request):
    return render(request, 'adminpanel/dashboard.html')

def login(request):
    return render(request, 'adminpanel/../templates/registration/login.html')