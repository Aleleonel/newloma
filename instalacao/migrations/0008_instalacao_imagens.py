# Generated by Django 3.1.3 on 2020-11-28 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instalacao', '0007_auto_20201128_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='instalacao',
            name='imagens',
            field=models.FileField(default=1, upload_to='media/%y/%m/%d/'),
            preserve_default=False,
        ),
    ]
