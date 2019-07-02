from django.shortcuts import render
from index.models import *
from contact.models import *

def index_contact(request):
    contacts = Contacts.objects.all()
    return render(request, "page/contact.html", {"contacts": contacts})
