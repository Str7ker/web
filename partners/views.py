from django.shortcuts import render
from index.models import *
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)
def index_partners(request):
    allpartners = AllPartner.objects.all()
    return render(request, "page/partners.html", {"allpartners": allpartners})
