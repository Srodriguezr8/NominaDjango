from django.shortcuts import render, redirect
from .models import TipoContrato
from .forms import TipoContratoForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup(request):
    if request.method == 'GET': 
        return render(request, 'signup.html', {
            'form' : UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('t_contrato:listado')
            except IntegrityError:
                return render(request, 'signup.html', {
            'form' : UserCreationForm,
            'error' : 'Usuario ya existente'
        })
        return render(request, 'signup.html', {
            'form' : UserCreationForm,
            'error' : 'No coincide la contraseña'
        })
            
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form' : AuthenticationForm
    })
    else:
        user = authenticate(request, username=request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
            'form' : AuthenticationForm,
            'error' : 'El usuario o la contraseña es incorrecta'
    })
        else:
            login(request, user)
            return redirect('t_contrato:listado')

@login_required
def tcontratos(request):
    dattcontrato = TipoContrato.objects.all()
    query = request.GET.get('q')
    if query:
        dattcontrato = TipoContrato.objects.filter(description__icontains=query)
    return render(request, 'tcontrato/listado.html', {
        'dattcontrato': dattcontrato, 
        'title': 'Listado de contratos'})

@login_required
def tcontrato_create(request):
    context = {'title' : 'Ingresar tipo contrato'}
    if request.method == 'GET':
        form = TipoContratoForm()
        context['form'] = form
        return render(request, 'tcontrato/create.html', context)
    else:
        form = TipoContratoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('t_contrato:listado')
        else:
            context['form'] = form
            return render(request, 'tcontrato/create.html')

@login_required
def tcontrato_update(request, id):
    context = {'title' : 'Actualizar tcontrato'}
    tcontrato = TipoContrato.objects.get(id=id)
    if request.method == 'GET':
        form = TipoContratoForm(instance=tcontrato)
        context['form'] = form
        return render(request, 'tcontrato/update.html', context)
    else:
        form = TipoContratoForm(request.POST, instance=tcontrato)
        if form.is_valid():
            form.save()
            return redirect('t_contrato:listado')
        else:
            context['form'] = form
            return render(request, 'tcontrato/update.html')

@login_required
def tcontrato_delete(request, id):
    from django.core.exceptions import ObjectDoesNotExist
    tcontrato = None
    try:
        tcontrato = TipoContrato.objects.get(id=id)
        if request.method == 'GET':
            context = {'title' : 'Tipo de Contrato a Eliminar', 'tcontrato' : tcontrato, 'error' : ''}
            return render(request, 'tcontrato/delete.html', context)
        else:
            tcontrato.delete()
            return redirect('t_contrato:listado')
    except ObjectDoesNotExist:
        context = {'title' : 'Tipo de contrato a Eliminar', 'tcontrato' : tcontrato, 'error' : 'Error al eliminar el tipo de contrato'}
        return render(request, 'tcontrato/delete.html', context)
    
     
@login_required   
def signout(request):
    logout(request)
    return redirect('inicio') 