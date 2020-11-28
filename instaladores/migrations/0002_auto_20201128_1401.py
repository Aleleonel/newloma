# Generated by Django 3.1.3 on 2020-11-28 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaladores', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instaladores',
            name='te01',
        ),
        migrations.RemoveField(
            model_name='instaladores',
            name='te02',
        ),
        migrations.AddField(
            model_name='instaladores',
            name='tel01',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='instaladores',
            name='tel02',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='instaladores',
            name='numero',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]