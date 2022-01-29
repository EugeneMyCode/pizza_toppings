from django import forms
from django import forms
from django.forms import widgets
from .models import Pizza, Topping

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['name']
        labels = {'name': ''}

class ToppingForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ['name']
        labels = {'name': 'Topping:'}
        widgets = {'name': forms.Textarea(attrs={'cols': 30})}
