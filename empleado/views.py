from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado
from .forms import EmpleadoForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

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
                return redirect('empleado:lista')
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
            return redirect('empleado:lista')


@login_required 
def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleado/lista.html', {'empleados': empleados})

@login_required 
def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empleado:lista')
    else:
        form = EmpleadoForm()
    return render(request, 'empleado/formulario.html', {'form': form})

@login_required 
def editar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('empleado:lista')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'empleado/formulario.html', {'form': form})

@login_required 
def eliminar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('empleado:lista')
    return render(request, 'empleado/confirmar_eliminar.html', {'empleado': empleado})

@login_required   
def signout(request):
    logout(request)
    return redirect('inicio') 