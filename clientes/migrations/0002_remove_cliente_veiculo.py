HEAD
# Generated by Django 3.1.3 on 2020-11-18 01:16

# Generated by Django 3.1.3 on 2020-11-19 01:24
busca

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='veiculo',
        ),
    ]
