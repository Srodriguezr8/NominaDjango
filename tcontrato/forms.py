from django.forms import ModelForm
from .models import TipoContrato

class TipoContratoForm(ModelForm):
    class Meta:
        model = TipoContrato
        fields = '__all__'