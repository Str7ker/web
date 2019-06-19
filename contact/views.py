from django.shortcuts import render
from index.models import *

def index_contact(request):
    logos = Logo.objects.all()
    return render(request, "page/contact.html", {"logos": logos})
