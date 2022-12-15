from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from tienda.models import Product, Cart



def addtocart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            if(product_check):
                if(Cart.objects.filter(user=request.user.id, product_id=prod_id)):
                    return JsonResponse({'status':'producto ya en el carro'})
                else:
                    prod_qty = int(request.POST.get('product_qty'))

                    if product_check.quantity >= prod_qty :
                        Cart.objects.create(user=request.user, product_id=prod_id, product_qty=prod_qty)
                        return JsonResponse({'status':'producto agregado correctamente'})
                    else:
                        return JsonResponse({'status':"Solo quedan "+ str(product_check.quantity)+ " unidades disponibles"})
            else:
               return JsonResponse({'status':'producto no encontrado'})
        else:
            return JsonResponse({'status':'Inicie sesion para continuar'})
        return redirect('/')

def viewcart(request):
    cart= Cart.objects.filter(user=request.user)
    context = {'cart':cart}
    return render(request, "tienda/cart.html", context)

def updatecart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user, product_id=prod_id)):
            prod_qty = int(request.POST.get('product_qty'))
            cart = Cart.objects.get(product_id=prod_id,user=request.user)
            cart.product_qty = prod_qty
            cart.save()
            return JsonResponse({'status':'Producto actualizado'})
    return redirect('/')

def deletecartitem(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user, product_id=prod_id)):
            cartitem = Cart.objects.get(product_id=prod_id, user=request.user)
            cartitem.delete()
        return JsonResponse({'status':'Producto eliminado'})
    return redirect('/')            