# Generated by Django 3.2.9 on 2022-04-25 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_alter_contribuinte_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='contribuinte',
            unique_together={('categoria', 'subCategoria', 'subSubCategoria', 'subSubSubCategoria', 'agencia', 'entidadeRepresentativa', 'nomeUpper', 'estatal', 'personalidade')},
        ),
    ]
