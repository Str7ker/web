from django import forms
from index.models import *
from team.models import *
class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('__all__')

class IndexPageForm(forms.ModelForm):

    class Meta:
        model = Romb
        fields = ('__all__')

class LogoForm(forms.ModelForm):

    class Meta:
        model = Logo
        fields = ('__all__')

class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ('__all__')

class WorkForm(forms.ModelForm):

    class Meta:
        model = Work
        fields = ('__all__')

class PartForm(forms.ModelForm):

    class Meta:
        model = Partner
        fields = ('__all__')

class PredForm(forms.ModelForm):

    class Meta:
        model = We_pred
        fields = ('__all__')

class TeamIndexForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ('__all__')

class AllPartnerForm(forms.ModelForm):

    class Meta:
        model = AllPartner
        fields = ('__all__')

class TeamsForm(forms.ModelForm):

    class Meta:
        model = Teams
        fields = ('__all__')