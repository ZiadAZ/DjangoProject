from django import forms
from .models import Brand,Product
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=200, widget=forms.PasswordInput())


  

    def authentication(self):

        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        is_authentication = authenticate(username=username, password=password)

        if is_authentication:
            return is_authentication
        return None

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