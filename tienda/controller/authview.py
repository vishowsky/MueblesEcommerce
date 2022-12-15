from django.shortcuts import redirect, render
from django.contrib import messages
from tienda.forms import CustomUserForm
from django.contrib.auth import authenticate, login, logout

def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
            form = CustomUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Registro completado satisfactoriamente, inicie sesion")
                return redirect('/login')
    context = {'form':form}
    return render (request, "tienda/auth/register.html", context)

def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request, "ya te encuentras loggeado")
        return redirect('/')
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')

            user= authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, "Inicio de sesion correcto")
                return redirect("/")
            else:
                messages.error(request, "Nombre de usuario o contraseña incorrecto")
                return redirect('/login')
    return render(request, "tienda/auth/login.html")

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Sesion cerrada correctamente")
    return redirect("/")
