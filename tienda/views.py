from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
def home(request):
    return render(request, "tienda/index.html")

def catalog(request):
    category = Category.objects.filter(status=0)
    context = {'category':category }
    return render(request, "tienda/catalog.html", context)

def catalogview(request ,slug):
    if(Category.objects.filter(slug=slug, status=0)):
        products = Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'products': products, 'category':category}
        return render(request, "tienda/products/index.html", context)
    else:
        messages.warning(request, "Categoria no encontrada")
        return redirect('catalog')

def productview(request, cate_slug, prod_slug):
    if(Category.objects.filter(slug=cate_slug, status=0)):
        if(Product.objects.filter(slug=prod_slug, status=0)):
            products = Product.objects.filter(slug=prod_slug, status=0).first
            context = {'products':products}
        else:
            messages.error(request, "Producto no encontrado")
            return redirect('catalog')
    else:
        messages.error(request, "Categoria no encontrada")
        return redirect('catalog')
    return render(request, "tienda/products/view.html", context)