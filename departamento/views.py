from django.shortcuts import render, redirect
from .models import Departamentos
from .forms import DepartamentoForm
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
                return redirect('departamento:listado')
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
            return redirect('departamento:listado')
        
          
@login_required
def listado(request):
    query = request.GET.get('q') # None
    departamentos = Departamentos.objects.all() #[{'id' : 1, 'description' : 'TICS'}, {'id' : 2, 'description' : 'Inspector'}]
    if query:
        departamentos = Departamentos.objects.filter(description__icontains=query)
    return render(request, 'departamento/listado.html', {
        'departamentos' : departamentos,
        'title' : 'Listado departamental'
    })

@login_required
def create(request):
    context = {'title': 'Ingresar Departamento'}
    if request.method == 'GET':
        form = DepartamentoForm()
        context['form'] = form #Crea una llave form y toma el valor de mi objeto formulario de departamento
        return render(request, 'departamento/create.html', context ) #{'title': 'Ingresar Departamento', 'form' : form}
    else:
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('departamento:listado')
        else:
            context['form'] = form
            return render(request, 'departamento/create.html')

@login_required
def update(request, id):
    context = {'title' : 'Actualizar Departamento'}
    departamento = Departamentos.objects.get(pk=id)
    if request.method == 'GET':
        form = DepartamentoForm(instance=departamento)
        context['form'] = form
        return render(request, 'departamento/update.html', context)
    else:
        form = DepartamentoForm(request.POST, instance=departamento)
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect('departamento:listado')

@login_required
def delete(request, id):
    departamento=None
    try:
        departamento = Departamentos.objects.get(pk=id)
        if request.method == "GET":
            context = {'title':'Eliminar :','departamento':departamento,'error':''}
            return render(request, 'departamento/delete.html',context)  
        else: 
            departamento.delete()
            return redirect('departamento:listado')
    except:
        context = {'title':'Departamento info','departamento':departamento,'error':'Error al eliminar departamento'}
        return render(request, 'departamento/delete.html',context)
 
@login_required   
def signout(request):
    logout(request)
    return redirect('inicio') 