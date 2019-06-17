from django.http import HttpResponseRedirect
from django.shortcuts import render
from index.models import *
from django.core.mail import send_mail
from django.views.generic import View
from django.core.mail import EmailMessage

def index(request):

    contact = Contact.objects.all()
    rombs = Romb.objects.all()
    cars = Car.objects.all()
    works = Work.objects.all()
    parts = Partner.objects.all()
    teams = Team.objects.all()
    preds = We_pred.objects.all()
    description = Description.objects.last()
    allpartners = AllPartner.objects.all()
    textteams = TextTeam.objects.all()
    return render(request, "index.html", {"contact": contact, "rombs": rombs, "cars": cars, "works": works, "parts": parts, "teams": teams, "textteams": textteams, "preds": preds,
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