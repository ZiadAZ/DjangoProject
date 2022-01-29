from django.shortcuts import get_object_or_404 , render

# Create your views here.
from django.http import HttpResponse
from .models import Brand,Product


def index(request):
    return render(request,'makeup/index.html')

def brandList(request):
    templateName='makeup/brand_list.html'
    list=Brand.objects.all()
    
    context={"name":"Brand","list":list}
    return render(request,templateName,context)

def productList(request):
    templateName='makeup/produc_list.html'
    list=Product.objects.all()
    
    context={"name":"Product","list":list}
    return render(request,templateName,context)

def brandDetail(request, id):
    templateName='makeup/brand_detail.html'
    context={"name":"Brand","brand":Brand.objects.get(pk=id)}
    return render(request,templateName,context)

def productDetail(request, id):
    templateName='makeup/product_detail.html'
    context={"name":"Product","product":get_object_or_404(Product,pk=id)}
    return render(request,templateName,context)

