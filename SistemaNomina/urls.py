"""
URL configuration for SistemaNomina project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from cargo.views import menu, signup, signout, signin

# from departamento.views import listado

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu, name='inicio' ),
    path('signupp/', signup, name='signup'),
    path('departamentos/',include('departamento.urls', namespace='departamento')),
    path('cargoss/', include('cargo.urls',namespace='cargo')),
    path('logout/', signout, name='logout'),
    path('signin/', signin, name='signin'),
    path('tcontratos/', include('tcontrato.urls',namespace='t_contrato')),
    path('rol/', include('rol.urls', namespace='rol')),
    path('empleado/', include('empleado.urls', namespace='empleado')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
