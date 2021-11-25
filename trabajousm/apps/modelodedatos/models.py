from enum import unique
from django.db import models
from django.db.models.fields import DateField

# Create your models here.
class Usuario (models.Model):
    usuRut= models.CharField(max_length=13, primary_key=True)
    usu_nombre = models.CharField(max_length=50)

class Funcionario (models.Model):
    funID = models.IntegerField(primary_key=True)
    funNombre = models.CharField( max_length=100)

class Prestamo(models.Model):
    preID = models.IntegerField(primary_key=True)
    usuRut = models.CharField(models.ForeignKey(Usuario, on_delete=models.CASCADE), max_length=13)
    funID = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    pre_fecha_hora = models.DateTimeField()
    pre_fecha_limite_retiro = models.DateField()
    pre_fecha_entrega = models.DateField()


class Penaliza(models.Model):
    peID = models.IntegerField(primary_key=True)
    preID = models.ForeignKey(Prestamo, on_delete=models.CASCADE)
    pe_fecha = models.DateField()
    pe_descripcion = models.CharField(max_length=200)
    pe_multa = models.IntegerField()
    pe_fecha_pago = models.DateField()
    pe_fecha_inicio = models.DateField()
    pe_fecha_fin = models.DateField()
    pe_vigente = models.BooleanField()



class Equipo(models.Model):
    eqID = models.IntegerField(primary_key=True)
    teqID = models.IntegerField()
    eqDescripcion = models.CharField( max_length=200)
    eq_fecha_ingreso = models.DateField()
    eq_nro_serie = models.CharField(max_length=100)
    eq_nro_inventario_usm = models.CharField( max_length=100)
    eq_fecha_baja = models.DateField()

class DetalleEquipo(models.Model):
    preID =models.ForeignKey(Prestamo,on_delete=models.CASCADE,unique=True)
    eqID = models.ForeignKey(Equipo, on_delete=models.CASCADE,unique=True)
    dp_fecha_hora_dev_sys = models.DateTimeField()
    dp_fecha_hora_dev_real = models.DateTimeField()
    dp_dias_suspension = models.IntegerField()

class UnidadMedida(models.Model):
    umID = models.IntegerField(primary_key=True)
    umNombre = models.CharField( max_length=25)

class Material(models.Model):
    matID= models.IntegerField(primary_key=True)
    umID = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)

class DetalleMaterial(models.Model):
    preID = models.ForeignKey(Prestamo, on_delete=models.CASCADE,unique=True)
    matID = models.ForeignKey(Material, on_delete=models.CASCADE, unique=True)

class TipoEquipo(models.Model):
    teqID = models.IntegerField(primary_key=True)
    teqNombre = models.CharField(max_length=50)
    teqDiasPrestamo = models.IntegerField()
    teqDiasSuspension = models.IntegerField()                         