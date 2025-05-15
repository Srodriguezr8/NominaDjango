from django.urls import path
from . import views
app_name = 'departamento'
urlpatterns = [
    path('departamento_list/', views.listado, name='listado'),
    path('departamento_create/', views.create, name='crear_departamento'),
    path('departamento_update/<int:id>/', views.update, name='actualizar_departamento'),
    path('departamento_delete/<int:id>/', views.delete, name='eliminar_departamento'),

]