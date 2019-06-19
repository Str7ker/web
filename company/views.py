from django.shortcuts import render
from index.models import *
from company.models import *

def index_company(request):
    logos = Logo.objects.all()
    companyes = Company.objects.all()
    preds = We_pred.objects.all()
    return render(request, "page/company.html", {"logos": logos, "companyes": companyes, "preds": preds})
