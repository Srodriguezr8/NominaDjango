from django.urls import path
from . import views
app_name = 't_contrato'
urlpatterns = [
    path('tcontratos_list/', views.tcontratos, name='listado'),
    path('tcontrato_create/', views.tcontrato_create, name='create'),
    path('tcontrato_update/<int:id>/', views.tcontrato_update, name='update'),
    path('tcontrato_delete/<int:id>/', views.tcontrato_delete, name='delete'),

]