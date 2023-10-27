from django import forms
from .models import Form


class MyForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = '__all__'
