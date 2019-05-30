from django.shortcuts import render

def index(request):
    data = {"header": "Привет", "text": "Ваня"}
    return render(request, "index.html", context=data)