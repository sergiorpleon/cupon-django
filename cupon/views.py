import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib import auth
from django.contrib.auth.decorators import login_required

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.db import models
from oferta.models import *
from ciudad.models import *

from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

def estatica(request, plantilla):
    # return HttpResponse("Ayuda")
    ciudades = Ciudad.objects.all()

    ciudadactual = ciudades[0]
    if "ciudad_actual" in request.session:
        ciudadactual = get_object_or_404(Ciudad, slug = request.session["ciudad_actual"])

    return render(request, plantilla, {'ciudadactual' : ciudadactual, 'ciudades': ciudades,})

@login_required
def contacto(request):
        # return HttpResponse("Ayuda")
    ciudades = Ciudad.objects.all()

    ciudadactual = ciudades[0]
    if "ciudad_actual" in request.session:
        ciudadactual = get_object_or_404(Ciudad, slug = request.session["ciudad_actual"])

    user = User.objects.get(username = request.user.username )
        
    
    if request.method == 'POST':
        subj = request.POST.get('subj', '')
        msg = request.POST.get('msg', '')
        
        user.email_user(subj, msg)

        return HttpResponseRedirect("/usuario/compras")
        
    return render(request, 'usuario/contacto.html', {'ciudadactual' : ciudadactual, 'ciudades': ciudades,})


# Create your views here.
def portada(request):
    # return HttpResponse("Ayuda")
    ciudades = Ciudad.objects.all()

    ciudadactual = ciudades[0]
    if "ciudad_actual" in request.session:
        ciudadactual = get_object_or_404(Ciudad, slug = request.session["ciudad_actual"])

    ahora = datetime.datetime.now()
    
    try:
        cercanas = Ciudad.objects.exclude(id=ciudadactual.id, )[0:5]
        relacionadas = Oferta.objects.exclude(ciudad_id=ciudadactual.id)
    
        oferta = Oferta.objects.filter(ciudad_id = ciudadactual.id).order_by("fecha_publicacion")[0:1].get()
        # si no hay oferta mostrar pagina ciudad sin oferta
    except Oferta.DoesNotExist:
        return render(request, 'oferta/nooferta.html', {'ciudadactual' : ciudadactual, 'ciudades': ciudades, 'relacionadas' : relacionadas, 'cercanas': cercanas})
    
    
    return render(request, 'oferta/portada.html', {'ciudadactual' : ciudadactual,'oferta': oferta, 'ciudades': ciudades, 'relacionadas' : relacionadas, 'cercanas': cercanas})

@login_required
def compras(request):
    # return HttpResponse("Ayuda")
    ciudades = Ciudad.objects.all()

    ciudadactual = ciudades[0]
    if "ciudad_actual" in request.session:
        ciudadactual = get_object_or_404(Ciudad, slug = request.session["ciudad_actual"])

    cercanas = Ciudad.objects.exclude(id=ciudadactual.id, )[0:5]
    compras = Venta.objects.filter(usuario_id= request.user.id)
    #relacionadas = Oferta.objects.filter(ciudad_id='1', )
    return render(request, 'usuario/compras.html', {'ciudadactual' : ciudadactual,'compras': compras, 'ciudades': ciudades, 'cercanas': cercanas})

def usuario(request):
    return render(request, 'usuario/compras.html', {'compras': compras, })

def login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Contrasena correcta y usuario marcado como "activo"
            auth.login(request, user)

            # Redireccciona a una pagina de entrada correcta.
            return HttpResponseRedirect("/usuario/compras")
        else:
            # Muestra una pagina de error
            return HttpResponseRedirect("/usuario/login")
    return render(request, 'usuario/login_form.html')


def logout(request):
    auth.logout(request)
    # Redireccciona a una pagina de entrada correcta.   
    return HttpResponseRedirect("/")


def registrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render(request, "usuario/registro.html", {
        'form': form,
    })

@login_required
def perfil(request):
    user = User.objects.get(username = request.user.username )
        
    if request.method == 'POST':
        firstname = request.POST.get('firstname', '')
        lastname = request.POST.get('lastname', '')
        email = request.POST.get('email', '')
        # password = request.POST.get('password', '')

        user.first_name = firstname
        user.last_name = lastname
        user.email = email
        # user.set_password(password)
        user.save()
        return HttpResponseRedirect("/usuario/compras")
        
    return render(request, 'usuario/perfil.html', {'firstname' : user.first_name, 'lastname' :  user.last_name, 'email' : user.email})


@login_required
def comprar(request, id):
    # return HttpResponse("Ayuda")
    ciudades = Ciudad.objects.all()

    try:
        ahora = datetime.datetime.now()

        user = User.objects.get(username = request.user.username )

        oferta = Oferta.objects.get(id=id, )
        oferta.compra = oferta.compra + 1
        oferta.save()

        venta = Venta(
            fecha = ahora,
    oferta = oferta,
    usuario = user
        )
        venta.save()
    except ObjectDoesNotExist:
        return HttpResponse("objeto no existe")

    ciudadactual = ciudades[0]
    if "ciudad_actual" in request.session:
        ciudadactual = get_object_or_404(Ciudad, slug = request.session["ciudad_actual"])

    cercanas = Ciudad.objects.exclude(id=ciudadactual.id, )[0:5]
    compras = Venta.objects.filter(usuario_id= request.user.id)
    #relacionadas = Oferta.objects.filter(ciudad_id='1', )
    return render(request, 'usuario/compras.html', {'ciudadactual' : ciudadactual,'compras': compras, 'ciudades': ciudades, 'cercanas': cercanas})
