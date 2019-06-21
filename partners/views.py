from django.shortcuts import render
from index.models import *

def index_partners(request):
    allpartners = AllPartner.objects.all()
    return render(request, "page/partners.html", {"allpartners": allpartners})
