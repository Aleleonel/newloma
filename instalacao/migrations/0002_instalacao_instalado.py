# Generated by Django 3.1.3 on 2020-11-24 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instalacao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instalacao',
            name='instalado',
            field=models.CharField(choices=[('SIM', 'SIM'), ('NÃO', 'NÃO'), ('PENDENTE', 'PENDENTE')], default='NÃO', max_length=8, null=True),
        ),
    ]
