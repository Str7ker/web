from django import forms
from index.models import *


class IndexPageForm(forms.ModelForm):

    class Meta:
        model = Romb
        fields = ('__all__')