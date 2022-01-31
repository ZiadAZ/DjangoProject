from django import forms
from .models import Brand,Product

class BrandForm(forms.Form):
    name=forms.CharField(label="Name",max_length=15)
    orgin=forms.CharField(label="orgin",max_length=15)

    def save(self):
     if self.is_valid():
        name=self.cleaned_data['name']
        orgin=self.cleaned_data['orgin']
        Brand.objects.create(name=name,orgin=orgin)
        return True
     return False