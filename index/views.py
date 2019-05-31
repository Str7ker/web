from django.shortcuts import render
from index.models import *

def index(request):
    contact = Contact.objects.all()
    rombs = Romb.objects.all()
    cars = Car.objects.all()
    works = Work.objects.all()
    parts = Partner.objects.all()
    preds = We_pred.objects.all()
    data = {"contact": contact, "rombs": rombs, "cars": cars, "works": works, "parts": parts, "preds": preds}
    return render(request, "index.html", context=data)

