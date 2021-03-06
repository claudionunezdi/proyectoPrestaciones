# Generated by Django 3.1.8 on 2021-11-23 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('eqID', models.IntegerField(primary_key=True, serialize=False)),
                ('teqID', models.IntegerField()),
                ('eqDescripcion', models.CharField(max_length=200)),
                ('eq_fecha_ingreso', models.DateField()),
                ('eq_nro_serie', models.CharField(max_length=100)),
                ('eq_nro_inventario_usm', models.CharField(max_length=100)),
                ('eq_fecha_baja', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('funID', models.IntegerField(primary_key=True, serialize=False)),
                ('funNombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoEquipo',
            fields=[
                ('teqID', models.IntegerField(primary_key=True, serialize=False)),
                ('teqNombre', models.CharField(max_length=50)),
                ('teqDiasPrestamo', models.IntegerField()),
                ('teqDiasSuspension', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UnidadMedida',
            fields=[
                ('umID', models.IntegerField(primary_key=True, serialize=False)),
                ('umNombre', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('usuRut', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('usu_nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('preID', models.IntegerField(primary_key=True, serialize=False)),
                ('usuRut', models.CharField(max_length=13, verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelodedatos.usuario'))),
                ('pre_fecha_hora', models.DateTimeField()),
                ('pre_fecha_limite_retiro', models.DateField()),
                ('pre_fecha_entrega', models.DateField()),
                ('funID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelodedatos.funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='Penaliza',
            fields=[
                ('peID', models.IntegerField(primary_key=True, serialize=False)),
                ('pe_fecha', models.DateField()),
                ('pe_descripcion', models.CharField(max_length=200)),
                ('pe_multa', models.IntegerField()),
                ('pe_fecha_pago', models.DateField()),
                ('pe_fecha_inicio', models.DateField()),
                ('pe_fecha_fin', models.DateField()),
                ('pe_vigente', models.BooleanField()),
                ('preID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelodedatos.prestamo')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('matID', models.IntegerField(primary_key=True, serialize=False)),
                ('umID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelodedatos.unidadmedida')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelodedatos.material', unique=True)),
                ('preID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelodedatos.prestamo', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleEquipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dp_fecha_hora_dev_sys', models.DateTimeField()),
                ('dp_fecha_hora_dev_real', models.DateTimeField()),
                ('dp_dias_suspension', models.IntegerField()),
                ('eqID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelodedatos.equipo', unique=True)),
                ('preID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelodedatos.prestamo', unique=True)),
            ],
        ),
    ]
