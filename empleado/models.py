from django.db import models
from departamento.models import Departamentos
from cargo.models import Cargo
from tcontrato.models import TipoContrato
# Create your models here.
class Empleado(models.Model):
    SEXO_CHOICES = [('M', 'Masculino'),('F', 'Femenino')]
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True)
    direccion = models.TextField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    cargo = models.ForeignKey(Cargo,on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamentos,on_delete=models.CASCADE)
    tipo_contrato = models.ForeignKey(TipoContrato,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.cedula}"