# Generated by Django 3.1.3 on 2020-11-28 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [

        ('endereco', '0001_initial'),

    ]

    operations = [
        migrations.CreateModel(
            name='Instaladores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                ('nome', models.CharField(max_length=60)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('rg', models.CharField(blank=True, max_length=9, null=True)),
                ('endereco', models.CharField(blank=True, max_length=60, null=True)),
                ('numero', models.CharField(blank=True, max_length=4, null=True)),
                ('te01', models.CharField(blank=True, max_length=9, null=True)),
                ('te02', models.CharField(blank=True, max_length=9, null=True)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
            options={
                'db_table': 'instaladores',
            },
        ),
    ]