# Generated by Django 3.1.3 on 2020-11-28 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instalacao', '0006_instalacao_vendedor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instalacao',
            old_name='ins_cliente',
            new_name='cliente',
        ),
        migrations.RenameField(
            model_name='instalacao',
            old_name='inst_data',
            new_name='data',
        ),
        migrations.RenameField(
            model_name='instalacao',
            old_name='inst_data_fim',
            new_name='data_fim',
        ),
        migrations.RenameField(
            model_name='instalacao',
            old_name='inst_instalador',
            new_name='instalador',
        ),
        migrations.RenameField(
            model_name='instalacao',
            old_name='inst_obs',
            new_name='obs',
        ),
        migrations.RenameField(
            model_name='instalacao',
            old_name='inst_placa',
            new_name='placa',
        ),
        migrations.RemoveField(
            model_name='instalacao',
            name='ins_contrato',
        ),
        migrations.AddField(
            model_name='instalacao',
            name='tel01',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='Celular'),
        ),
        migrations.AddField(
            model_name='instalacao',
            name='tel02',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='Fone Res.'),
        ),
        migrations.AddField(
            model_name='instalacao',
            name='vistoria',
            field=models.CharField(choices=[('SIM', 'SIM'), ('NÃO', 'NÃO'), ('PENDENTE', 'PENDENTE')], default='NÃO', max_length=8, null=True),
        ),
    ]
