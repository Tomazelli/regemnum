# Generated by Django 3.2.9 on 2022-01-05 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20220104_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitoracao',
            name='monitorar',
            field=models.CharField(default='#', max_length=100, unique=True, verbose_name='Monitorar'),
        ),
    ]