# Generated by Django 3.1.3 on 2020-11-28 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaladores', '0004_merge_20201128_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instaladores',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=4),
            preserve_default=False,
        ),
    ]
