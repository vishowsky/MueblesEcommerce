from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from tienda.models import Cart, Order, OrderItem,Product, Profile
from django.contrib.auth.models import User
from django.conf import settings
import random

@login_required(login_url='loginpage')
def index(request):
    rawcart = Cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_qty > item.product.quantity:
            Cart.objects.delete(id=item.id)
    cartitems = Cart.objects.filter(user=request.user)
    total_price = 1
    for item in cartitems:
        total_price = total_price * item.product.final_price * item.product_qty

    userprofile = Profile.objects.filter(user=request.user).first()
   

    context = {'cartitems':cartitems, 'total_price':total_price, 'userprofile':userprofile}
    return render(request, "tienda/checkout.html", context)

@login_required(login_url='loginpage')
def placeorder(request):
    if request.method == 'POST':

        currentuser = User.objects.filter(id=request.user.id).first()

        if not currentuser.first_name:
            currentuser.first_name = request.POST.get('fname')
            currentuser.first_name = request.POST.get('lname')
            currentuser.first_name = request.POST.get('rut')
            currentuser.save()

        if not Profile.objects.filter(user=request.user):
            userprofile = Profile()
            userprofile.user = request.user
            userprofile.rut = request.POST.get('rut')
            userprofile.email = request.POST.get('email')
            userprofile.phone = request.POST.get('phone')
            userprofile.address = request.POST.get('address')
            userprofile.city = request.POST.get('city')
            userprofile.region = request.POST.get('region')
            userprofile.save()


        neworder = Order()
        neworder.user = request.user
        neworder.fname = request.POST.get('fname')
        neworder.lname = request.POST.get('lname')
        neworder.rut = request.POST.get('rut')
        neworder.email = request.POST.get('email')
        neworder.phone = request.POST.get('phone')
        neworder.address = request.POST.get('address')
        neworder.city = request.POST.get('city')
        neworder.region = request.POST.get('region')
       
        neworder.payment_mode = request.POST.get('payment_mode')
        cart = Cart.objects.filter(user=request.user)
        cart_total_price = 0
        for item in cart:
            cart_total_price = cart_total_price + item.product.final_price * item.product_qty

        neworder.total_price = cart_total_price
        trackno = str(random.randint(1111111,9999999))
        while Order.objects.filter(tracking_no=trackno):
            trackno =str(random.randint(1111111,9999999))

        neworder.tracking_no = trackno
        neworder.save()

        neworderitems = Cart.objects.filter(user=request.user)
        for item in neworderitems:
            OrderItem.objects.create(
                order=neworder,
                product=item.product,
                price= item.product.final_price,
                quantity=item.product_qty

            )
            orderproduct= Product.objects.filter(id=item.product_id).first()
            orderproduct.quantity = orderproduct.quantity - item.product_qty
            orderproduct.save()
            

            Cart.objects.filter(user=request.user).delete()

            messages.success(request, "El pedido fue completado con exito")
    return redirect('/')
