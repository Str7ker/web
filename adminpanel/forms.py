from django import forms
from index.models import *
from team.models import *
from company.models import *
from contact.models import *
from adminpanel.models import Admin_main

class AmForm(forms.ModelForm):

    class Meta:
        model = Admin_main
        fields = ('title1', 'title2', 'url', 'count', 'color', 'ico', 'date_add', 'date_edit')

class ContactForm(forms.ModelForm):
    phone = forms.CharField(label="Телефон", widget=forms.TextInput(attrs={"id": "phone-number"}))
    class Meta:
        model = Contact
        fields = ('phone', 'email', 'address_fact', 'vk', 'insta', 'date_add', 'date_edit')

class IndexPageForm(forms.ModelForm):

    class Meta:
        model = Romb
        fields = ('name_romb', 'ico', 'text', 'numbers', 'date_add', 'date_edit')

class LogoForm(forms.ModelForm):

    class Meta:
        model = Logo
        fields = ('small_logo', 'logo', 'background', 'date_add', 'date_edit')

class CarForm(forms.ModelForm):
    text = forms.CharField(label="Текст", widget=forms.Textarea(attrs={"id": "summernote"}))
    class Meta:
        model = Car
        fields = ('name_cars', 'img', 'name', 'text', 'date_add', 'date_edit')

class WorkForm(forms.ModelForm):
    text = forms.CharField(label="Текст", widget=forms.Textarea(attrs={"id": "summernote"}))
    class Meta:
        model = Work
        fields = ('name_work', 'img', 'name', 'text', 'date_add', 'date_edit')

class PartForm(forms.ModelForm):

    class Meta:
        model = Partner
        fields = ('name_part', 'img', 'date_add', 'date_edit')

class PredForm(forms.ModelForm):

    class Meta:
        model = We_pred
        fields = ('name_pred', 'img', 'text', 'date_add', 'date_edit')

class TeamIndexForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ('img', 'name', 'position', 'phone', 'mail', 'date_add', 'date_edit')

class AllPartnerForm(forms.ModelForm):
    number = forms.CharField(label="Телефон", widget=forms.TextInput(attrs={"id": "phone-number"}))
    class Meta:
        model = AllPartner
        fields = ('name_part', 'img', 'text', 'number', 'email', 'date_add', 'date_edit')

class TeamsForm(forms.ModelForm):
    phone = forms.CharField(label="Телефон", widget=forms.TextInput(attrs={"id": "phone-number"}))
    class Meta:
        model = Teams
        fields = ('img', 'name', 'position', 'phone', 'mail', 'date_add', 'date_edit', 'date_add', 'date_edit')

class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ('title', 'small_text', 'big_text', 'date_add', 'date_edit')

class ContactsForm(forms.ModelForm):
    phone = forms.CharField(label="Телефон", widget=forms.TextInput(attrs={"id": "phone-number"}))
    email = forms.CharField(label="Электронная почта", widget=forms.TextInput(attrs={"id": "email"}))
    class Meta:
        model = Contacts
        fields = ('phone', 'email', 'address_fact', 'vk', 'insta', 'inn', 'ogrn', 'kpp', 'img', 'date_add', 'date_edit')