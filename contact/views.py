from django.shortcuts import render
from index.models import *
from contact.models import *
from django.views.decorators.cache import cache_page
from django.http import HttpResponse
from django.views.generic.base import TemplateView, RedirectView
from django.shortcuts import get_object_or_404, reverse



class Contact(TemplateView):
    template_name = "page/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = Contacts.objects.all()
        return context

@cache_page(60 * 15)
def index_contact(request):
    contacts = Contacts.objects.all()
    return render(request, "page/contact.html", {"contacts": contacts})