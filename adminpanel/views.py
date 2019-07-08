
import os
import os.path
from web.settings import BASE_DIR
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from adminpanel.forms import *
from adminpanel.models import Admin_main
from company.models import *
from contact.models import *
from index.models import *
from team.models import *
from django.core.cache import cache
from django.shortcuts import reverse

# @cache_page(60 * 15)
# @login_required
# def dashboard(request):
#     order = Order.objects.all()
#     return render(request, 'adminpanel/dashboard.html', {'order': order, })

# --------------- Главная

# @cache_page(60 * 15)
@login_required
def board(request):
    teams = Teams.objects.all().count()
    part = Partner.objects.all().count()
    pred = We_pred.objects.all().count()
    am = Admin_main.objects.all()
    if request.method == 'POST':
        am_form = AmForm(request.POST)
        if am_form.is_valid():
            am_form.save()
            return HttpResponseRedirect('/panel/')
    else:
        am_form = AmForm()
    return render(request, 'adminpanel/board.html',
                  {
                      "teams": teams, "part": part, "pred": pred, "am_form": am_form, "am": am,
                  })

@cache_page(60 * 15)
@login_required
def board_edit(request, pk):
    teams = Teams.objects.all().count()
    part = Partner.objects.all().count()
    pred = We_pred.objects.all().count()
    ams = Admin_main.objects.get(pk=pk)
    if request.method == 'POST':
        am_form = AmForm(request.POST, request.FILES, instance=ams)
        if am_form.is_valid():
            ams = am_form.save(commit=False)
            ams.date_edit = datetime.now()
            am_form.save()
            return HttpResponseRedirect('/panel/')
    else:
        am_form = AmForm(instance=ams)
    return render(request, 'adminpanel/board_edit.html',
                  {
                      "teams": teams, "part": part, "pred": pred, "am_form": am_form, "ams": ams,
                  })

@cache_page(60 * 15)
@login_required
def board_del(request, pk):
    Admin_main.objects.get(pk=pk).delete()
    return HttpResponseRedirect('/panel/')
# --------------- Контакты

# @cache_page(60 * 15)
@login_required
def dashboard(request):
    contact = Contact.objects.get(pk=2)
    if request.method == 'POST':
        contact_form = ContactForm(request.POST, request.FILES, instance=contact)
        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.date_edit = datetime.now()
            contact_form.save()
            return HttpResponseRedirect('/panel/contact/')
    else:
        contact_form = ContactForm(instance=contact)
    return render(request, 'adminpanel/dashboard.html', {'contact_form': contact_form, 'contact': contact})


@cache_page(60 * 15)
@login_required
def dashboard_del(request, pk):
    Contact.objects.get(pk=pk).delete()
    return HttpResponseRedirect('/panel/contact/')


# --------------- Ромбы
# @cache_page(60 * 15)
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
    return render(request, 'adminpanel/page_index.html', {'romb_form': romb_form, 'romb': romb})


@cache_page(60 * 15)
@login_required
def page_index_edit(request, pk):
    rombs = Romb.objects.get(pk=pk)
    if request.method == 'POST':
        romb_forms = IndexPageForm(request.POST, request.FILES, instance=rombs)
        if romb_forms.is_valid():
            romb = romb_forms.save(commit=False)
            romb.date_edit = datetime.now()
            romb_forms.save()
            return HttpResponseRedirect('/panel/page_index/')
    else:
        romb_forms = IndexPageForm(instance=rombs)
    return render(request, 'adminpanel/page_index_edit.html', {'romb_forms': romb_forms, 'rombs': rombs})


@cache_page(60 * 15)
@login_required
def page_index_del(request, pk):
    Romb.objects.get(pk=pk).delete()
    return HttpResponseRedirect('/panel/page_index/')


# --------------- Лого

@cache_page(60 * 15)
@login_required
def logo(request):
    logo = Logo.objects.all()
    if request.method == 'POST':
        logo_form = LogoForm(request.POST, request.FILES)
        if logo_form.is_valid():
            logo = logo_form.save(commit=False)
            logo.date_edit = datetime.now()
            logo_form.save()
            return HttpResponseRedirect('/panel/logo/')
    else:
        logo_form = LogoForm()
    return render(request, 'adminpanel/logo.html', {'logo_form': logo_form, 'logo': logo})


@cache_page(60 * 15)
@login_required
def logo_del(request, pk):
    Logo.objects.get(pk=pk).delete()
    return HttpResponseRedirect('/panel/logo/')


# --------------- Грузоперевозки

# @cache_page(60 * 15)
@login_required
def gruz(request):
    cars = Car.objects.all()
    if request.method == 'POST':
        gruz_form = CarForm(request.POST, request.FILES)
        if gruz_form.is_valid():
            gruz_form.save()
            return HttpResponseRedirect('/panel/gruz/')
    else:
        gruz_form = CarForm()
    return render(request, 'adminpanel/gruz.html', {'gruz_form': gruz_form, 'cars': cars})


@cache_page(60 * 15)
@login_required
def gruz_edit(request, pk):
    cars = Car.objects.get(pk=pk)
    if request.method == 'POST':
        gruz_form = CarForm(request.POST, request.FILES, instance=cars)
        if gruz_form.is_valid():
            gruz = gruz_form.save(commit=False)
            gruz.date_edit = datetime.now()
            gruz_form.save()
            return HttpResponseRedirect('/panel/gruz/')
    else:
        gruz_form = CarForm(instance=cars)
    return render(request, 'adminpanel/gruz_edit.html', {'gruz_form': gruz_form, 'cars': cars})


@cache_page(60 * 15)
@login_required
def gruz_del(request, pk):
    Car.objects.get(pk=pk).delete()
    return HttpResponseRedirect('/panel/gruz/')


# --------------- Как мы работаем

# @cache_page(60 * 15)
@login_required
def work(request):
    works = Work.objects.all()
    if request.method == 'POST':
        work_form = WorkForm(request.POST, request.FILES)
        if work_form.is_valid():
            work_form.save()
            return HttpResponseRedirect('/panel/work/')
    else:
        work_form = WorkForm()
    return render(request, 'adminpanel/work.html', {'work_form': work_form, 'works': works})


@cache_page(60 * 15)
@login_required
def work_edit(request, pk):
    work = Work.objects.get(pk=pk)
    if request.method == 'POST':
        work_forms = WorkForm(request.POST, request.FILES, instance=work)
        if work_forms.is_valid():
            work = work_forms.save(commit=False)
            work.date_edit = datetime.now()
            work_forms.save()
            return HttpResponseRedirect('/panel/work/')
    else:
        work_forms = WorkForm(instance=work)
    return render(request, 'adminpanel/work_edit.html', {'work_forms': work_forms, 'work': work})


@cache_page(60 * 15)
@login_required
def work_del(request, pk):
    Work.objects.get(pk=pk).delete()
    return HttpResponseRedirect('/panel/work/')


# --------------- Партнёры на главной

# @cache_page(60 * 15)
@login_required
def part(request):
    parts = Partner.objects.all()
    if request.method == 'POST':
        part_form = PartForm(request.POST, request.FILES)
        if part_form.is_valid():
            part_form.save()
            return HttpResponseRedirect('/panel/part/')
    else:
        part_form = PartForm()
    return render(request, 'adminpanel/part.html', {'part_form': part_form, 'parts': parts})


@cache_page(60 * 15)
@login_required
def part_edit(request, pk):
    part = Partner.objects.get(pk=pk)
    if request.method == 'POST':
        parts_form = PartForm(request.POST, request.FILES, instance=part)
        if parts_form.is_valid():
            part = parts_form.save(commit=False)
            part.date_edit = datetime.now()
            parts_form.save()
            return HttpResponseRedirect('/panel/part/')
    else:
        parts_form = PartForm(instance=part)
    return render(request, 'adminpanel/part_edit.html', {'parts_form': parts_form, 'part': part})


@cache_page(60 * 15)
@login_required
def part_del(request, pk):
    Partner.objects.get(pk=pk).delete()
    return HttpResponseRedirect('/panel/part/')


# --------------- Мы предоставляем

# @cache_page(60 * 15)
@login_required
def pred(request):
    preds = We_pred.objects.all()
    if request.method == 'POST':
        pred_form = PredForm(request.POST, request.FILES)
        if pred_form.is_valid():
            pred_form.save()
            return HttpResponseRedirect('/panel/pred/')
    else:
        pred_form = PredForm()
    return render(request, 'adminpanel/pred.html', {'pred_form': pred_form, 'preds': preds})


@cache_page(60 * 15)
@login_required
def pred_edit(request, pk):
    pred = We_pred.objects.get(pk=pk)
    if request.method == 'POST':
        pred_form = PredForm(request.POST, request.FILES, instance=pred)
        if pred_form.is_valid():
            pred = pred_form.save(commit=False)
            pred.date_edit = datetime.now()
            pred_form.save()
            return HttpResponseRedirect('/panel/pred/')
    else:
        pred_form = PredForm(instance=pred)
    return render(request, 'adminpanel/pred_edit.html', {'pred_form': pred_form, 'pred': pred})


@cache_page(60 * 15)
@login_required
def pred_del(request, pk):
    We_pred.objects.get(pk=pk).delete()
    return HttpResponseRedirect('/panel/pred/')


# --------------- Сотрудники на главной

# @cache_page(60 * 15)
@login_required
def team_index(request):
    team_index = Team.objects.all()
    if request.method == 'POST':
        team_index_form = TeamIndexForm(request.POST, request.FILES)
        if team_index_form.is_valid():
            team_index_form.save()
            return HttpResponseRedirect('/panel/team_index/')
    else:
        team_index_form = TeamIndexForm()
    return render(request, 'adminpanel/team_index.html', {'team_index_form': team_index_form, 'team_index': team_index})


@cache_page(60 * 15)
@login_required
def team_index_edit(request, pk):
    team_index = Team.objects.get(pk=pk)
    if request.method == 'POST':
        team_index_form = TeamIndexForm(request.POST, request.FILES, instance=team_index)
        if team_index_form.is_valid():
            team = team_index_form.save(commit=False)
            team.date_edit = datetime.now()
            team_index_form.save()
            return HttpResponseRedirect('/panel/team_index/')
    else:
        team_index_form = TeamIndexForm(instance=team_index)
    return render(request, 'adminpanel/team_index_edit.html',
                  {'team_index_form': team_index_form, 'team_index': team_index})


@cache_page(60 * 15)
@login_required
def team_index_del(request, pk):
    Team.objects.get(pk=pk).delete()
    return HttpResponseRedirect('/panel/team_index/')


# --------------- Партнёры

# @cache_page(60 * 15)
@login_required
def partners(request):
    partners = AllPartner.objects.all()
    if request.method == 'POST':
        partners_form = AllPartnerForm(request.POST, request.FILES)
        if partners_form.is_valid():
            partners_form.save()
            return HttpResponseRedirect('/panel/partners/')
    else:
        partners_form = AllPartnerForm()
    return render(request, 'adminpanel/partners.html', {'partners_form': partners_form, 'partners': partners})


@cache_page(60 * 15)
@login_required
def partners_edit(request, pk):
    partner = AllPartner.objects.get(pk=pk)
    if request.method == 'POST':
        partner_form = AllPartnerForm(request.POST, request.FILES, instance=partner)
        if partner_form.is_valid():
            part = partner_form.save(commit=False)
            part.date_edit = datetime.now()
            partner_form.save()
            return HttpResponseRedirect('/panel/partners/')
    else:
        partner_form = AllPartnerForm(instance=partner)
    return render(request, 'adminpanel/partners_edit.html', {'partner_form': partner_form, 'partner': partner})


@cache_page(60 * 15)
@login_required
def partners_del(request, pk):
    AllPartner.objects.get(pk=pk).delete()
    return HttpResponseRedirect('/panel/partners/')


# --------------- Сотрудники


# @cache_page(60 * 15)
@login_required
def teams(request):
    teams = Teams.objects.all()
    if request.method == 'POST':
        teams_form = TeamsForm(request.POST, request.FILES)
        if teams_form.is_valid():
            teams_form.save()
            return HttpResponseRedirect('/panel/teams/')
    else:
        teams_form = TeamsForm()
    return render(request, 'adminpanel/teams.html', {'teams_form': teams_form, 'teams': teams})


@cache_page(60 * 15)
@login_required
def teams_edit(request, pk):
    team = Teams.objects.get(pk=pk)
    if request.method == 'POST':
        team_form = TeamsForm(request.POST, request.FILES, instance=team)
        if team_form.is_valid():
            team = team_form.save(commit=False)
            team.date_edit = datetime.now()
            team_form.save()
            return HttpResponseRedirect('/panel/teams/')
    else:
        team_form = TeamsForm(instance=team)
    return render(request, 'adminpanel/teams_edit.html', {'team_form': team_form, 'team': team})


@cache_page(60 * 15)
@login_required
def teams_del(request, pk):
    Teams.objects.get(pk=pk).delete()
    return HttpResponseRedirect('/panel/teams/')


# --------------- Компания
@cache_page(60 * 15)
@login_required
def company(request):
    company = Company.objects.get(pk=1)
    if request.method == 'POST':
        company_form = CompanyForm(request.POST, request.FILES, instance=company)
        if company_form.is_valid():
            company = company_form.save(commit=False)
            company.date_edit = datetime.now()
            company_form.save()
            return HttpResponseRedirect('/panel/company/')
    else:
        company_form = CompanyForm(instance=company)
    return render(request, 'adminpanel/company.html', {'company_form': company_form, 'company': company})


@cache_page(60 * 15)
@login_required
def company_del(request, pk):
    Company.objects.get(pk=pk).delete()
    return HttpResponseRedirect('/panel/company/')


# --------------- Контакты

@cache_page(60 * 15)
@login_required
def contacts(request):
    contacts = Contacts.objects.get(pk=1)
    if request.method == 'POST':
        contacts_form = ContactsForm(request.POST, request.FILES, instance=contacts)
        if contacts_form.is_valid():
            contact = contacts_form.save(commit=False)
            contact.date_edit = datetime.now()
            contacts_form.save()
            return HttpResponseRedirect('/panel/contacts/')
    else:
        contacts_form = ContactsForm(instance=contacts)
    return render(request, 'adminpanel/contacts.html', {'contacts_form': contacts_form, 'contacts': contacts})


@cache_page(60 * 15)
@login_required
def contacts_del(request, pk):
    Contacts.objects.get(pk=pk).delete()
    return HttpResponseRedirect('/panel/contacts/')


# Управление

@login_required
def settings(request):
    if request.method == 'POST':
        cache.clear()
        return HttpResponseRedirect(reverse('settings'))
    else:
        return render(request, 'adminpanel/settings.html')
