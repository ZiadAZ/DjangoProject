from django.shortcuts import get_object_or_404 , render

# Create your views here.
from django.http import HttpResponse
from .models import Brand,Product
from .forms import BrandForm,ProductForm
from django.http import HttpResponseRedirect

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



def brandCreate(request,id=None):
    form=BrandForm

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BrandForm(request.POST)
        # check whether it's valid:
        
        if form.save():
            
            return brandList(request)
    elif id :
        obj = get_object_or_404(Brand, pk = id)
        form = BrandForm( {'name':obj.name,'orgin':obj.orgin})
        
    templateName='makeup/brand_create.html'
    context={"name":"Brand","form":form}
    return render(request,templateName,context)
    


def brandDelete(request, id):
        get_object_or_404(Brand, pk = id).delete()
 
        return brandList(request)

def productManage(request,id=None):
    form=ProductForm

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProductForm(request.POST)
        # check whether it's valid:
        
        if form.save():
            
            return productList(request)
    elif id :
        obj = get_object_or_404(Product, pk = id)
        form = ProductForm( {'name':obj.name,'orgin':obj.orgin})
        
    templateName='makeup/product_manage.html'
    context={"name":"Product","form":form}
    return render(request,templateName,context)
 

def productDelete(request, id):
        get_object_or_404(Product, pk = id).delete()
 
        return productList(request)