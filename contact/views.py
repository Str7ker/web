from django.shortcuts import render

def index_contact(request):
    return render(request, "page/contact.html", {"bla": "bla"})
