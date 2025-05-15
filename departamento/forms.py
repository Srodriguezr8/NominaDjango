from django.forms import ModelForm
from .models import Departamentos


class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamentos
        fields = '__all__'
