# Generated by Django 3.2.9 on 2022-04-25 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20220425_1941'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='contribuinte',
            unique_together={('categoria', 'subCategoria', 'subSubCategoria', 'subSubSubCategoria', 'agencia', 'entidadeRepresentativa', 'nome', 'estatal', 'personalidade'), ('categoria', 'subCategoria', 'subSubCategoria', 'subSubSubCategoria', 'agencia', 'entidadeRepresentativa', 'nomeUpper', 'estatal', 'personalidade')},
        ),
    ]