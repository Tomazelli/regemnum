# Generated by Django 3.2.9 on 2022-04-24 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_subcategoriasparticipante_subcategoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contribuinte',
            name='personalidade',
            field=models.CharField(max_length=4, verbose_name='Personalidade'),
        ),
    ]