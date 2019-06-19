from django.shortcuts import render
from index.models import *

def index_movizor(request):
    logos = Logo.objects.all()
    return render(request, "page/movizor.html", {"logos": logos})

