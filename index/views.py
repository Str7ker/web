from django.http import HttpResponseRedirect
from django.shortcuts import render
from index.models import *
from django.core.mail import send_mail
from django.views.generic import View


class MyFormView(View):
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):

        contact = Contact.objects.all()
        rombs = Romb.objects.all()
        cars = Car.objects.all()
        works = Work.objects.all()
        parts = Partner.objects.all()
        preds = We_pred.objects.all()
        description = Description.objects.last()
        return render(request, self.template_name, {"contact": contact, "rombs": rombs, "cars": cars, "works": works, "parts": parts, "preds": preds,
            "description": description})


    def post(self, request, *args, **kwargs):
        email = request
        send_mail('Subject here', 'Here is the message.', 'stryker.aaaa@yandex.ru',
            ['stryker.aaaa@yandex.ru'], fail_silently=False)
