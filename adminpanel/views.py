from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from adminpanel.forms import *
from index.models import *
from django.http import HttpResponseRedirect
@login_required
def dashboard(request):
    order = Order.objects.all()
    return render(request, 'adminpanel/dashboard.html', {'order': order, })

@login_required
def page_index(request):
    romb = Romb.objects.all()
    if request.method == 'POST':
        romb_form = IndexPageForm(request.POST)
        if romb_form.is_valid():
            romb_form.save()
            return HttpResponseRedirect('/panel/page_index/')
    else:
        romb_form = IndexPageForm()
    return render(request, 'adminpanel/pade_index.html', {'romb_form': romb_form, 'romb': romb})

@login_required
def page_index_del(request, pk):
    Romb.objects.get(pk=pk).delete()
    return HttpResponseRedirect('/panel/page_index/')
