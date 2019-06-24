from django import forms
from index.models import Order


class OrderForm(forms.ModelForm):
    name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}))
    phone = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Ваш  телефон'}))
    email = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Ваша электронная почта'}))
    class Meta:
        model = Order
        fields = ('__all__')