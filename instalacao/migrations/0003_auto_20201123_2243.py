# Generated by Django 3.1.3 on 2020-11-24 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instaladores', '0002_auto_20201122_1232'),
        ('instalacao', '0002_instalacao_instalado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instalacao',
            name='inst_instalador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='instaladores.instaladores'),
        ),
    ]
