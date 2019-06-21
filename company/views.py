from django.shortcuts import render
from index.models import *
from company.models import *

def index_company(request):
    companyes = Company.objects.all()
    preds = We_pred.objects.all()
    return render(request, "page/company.html", {"companyes": companyes, "preds": preds})
