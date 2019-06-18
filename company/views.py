from django.shortcuts import render

def index_company(request):
    return render(request, "page/company.html", {"bla": "bla"})
