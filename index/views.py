from django.http import HttpResponseRedirect
from django.shortcuts import render
from index.models import *
from django.core.mail import send_mail
from django.views.generic import View
from django.core.mail import EmailMessage
from index.forms import OrderForm,EmailForm
from django.views.decorators.cache import cache_page

# @cache_page(60 * 15)
def index(request):

    contact = Contact.objects.all()
    rombs = Romb.objects.all()
    cars = Car.objects.all()
    works = Work.objects.all()
    parts = Partner.objects.all()
    teams_index = Team.objects.all()
    preds = We_pred.objects.all()
    description = Description.objects.last()
    allpartners = AllPartner.objects.all()
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_form.save()
            return HttpResponseRedirect('/')
    else:
        order_form = OrderForm()
    if request.method == 'POST':
        email_form = EmailForm(request.POST)
        if email_form.is_valid():
            email_form.save()
            return HttpResponseRedirect('/')
    else:
        email_form = EmailForm()

    return render(request, "index.html", {"order_form": order_form, "email_form": email_form, "contact": contact, "rombs": rombs, "cars": cars, "works": works, "parts": parts, "teams_index": teams_index, "preds": preds,
            "description": description, "allpartners": allpartners})


def mailss(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        telephone = request.POST.get("telephone")
        # send_mail('Заявка', name + '<br/> ' + email + '<br/> ' + telephone, email,
        #     ['stryker.aaaa@yandex.ru'], fail_silently=False)
        msg = EmailMessage(
            'Новая заявка ' + name,
            'Имя клиента: ' + name + '<br>'
            'Электронная почта клиента: ' + email + '<br>'
            'Номер телефона клиента: ' + telephone + '<br>',
            "info@plce.top",
            ['stryker.aaaa@yandex.ru', ]
        )
        msg.content_subtype = "html"
        msg.send()
        print(name, email, telephone)
    return HttpResponseRedirect("http://127.0.0.1:8000")