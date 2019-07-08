from django.shortcuts import render
from index.models import *
from company.models import *
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)
def index_company(request):
    companyes = Company.objects.all()
    preds = We_pred.objects.all()
    return render(request, "page/company.html", {"companyes": companyes, "preds": preds})
