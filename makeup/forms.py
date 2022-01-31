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

class ProductForm(forms.Form):
    name=forms.CharField(label="Name",max_length=15)
    kind=forms.CharField(label="kind",max_length=50)
    descreption = forms.CharField(label="descreption",max_length=50)
    expirDate= forms.DateField(label="expirDate")
    price=forms.IntegerField(label="price")
    brand = forms.ModelChoiceField(queryset=Brand.objects.all())

    def save(self):
     if self.is_valid():
        name=self.cleaned_data['name']
        kind=self.cleaned_data['kind']
        descreption = self.cleaned_data['descreption']
        expirDate= self.cleaned_data['expirDate']
        price=self.cleaned_data['price']
        brand =self.cleaned_data['brand']
        Product.objects.create(name=name,kind=kind,descreption=descreption,expirDate=expirDate,price=price,brand=brand)
        return True
     return False