# Generated by Django 3.1.3 on 2020-11-24 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instalacao', '0003_auto_20201123_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instalacao',
            name='user',
            field=models.CharField(max_length=30),
        ),
    ]
