# Generated by Django 3.1.3 on 2020-11-28 22:24

from django.db import migrations, models
import instalacao.models


class Migration(migrations.Migration):

    dependencies = [
        ('instalacao', '0009_auto_20201128_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instalacao',
            name='imagens',
            field=models.FileField(upload_to=instalacao.models.get_file_path),
        ),
    ]
