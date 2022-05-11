# Generated by Django 3.2.9 on 2022-04-13 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_mecanismodeparticipacao_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contribuicoesporparticipante',
            name='linkAnexo',
            field=models.CharField(default='#', max_length=208, verbose_name='Link para o anexo'),
        ),
        migrations.AlterField(
            model_name='contribuicoesporparticipante',
            name='linkContribuicao',
            field=models.CharField(max_length=206, verbose_name='Link das contribuições'),
        ),
        migrations.AlterField(
            model_name='contribuicoesporparticipante',
            name='linkResultado',
            field=models.CharField(default='#', max_length=207, verbose_name='Link para os resultados'),
        ),
        migrations.AlterField(
            model_name='contribuicoesporparticipante',
            name='pessoaFisica',
            field=models.CharField(default='#', max_length=205, verbose_name='Nome das pessoas fisicas'),
        ),
        migrations.AlterField(
            model_name='contribuinte',
            name='nome',
            field=models.CharField(max_length=204, verbose_name='Nome do contribuinte'),
        ),
        migrations.AlterField(
            model_name='documentomanifestacao',
            name='linkDocumento',
            field=models.CharField(max_length=209, verbose_name='Link do documento'),
        ),
        migrations.AlterField(
            model_name='documentomanifestacao',
            name='referencia',
            field=models.CharField(max_length=210, verbose_name='Referencia'),
        ),
        migrations.AlterField(
            model_name='mecanismodeparticipacao',
            name='indexacaoSubtema',
            field=models.CharField(max_length=203, verbose_name='Indexação subtema'),
        ),
        migrations.AlterField(
            model_name='mecanismodeparticipacao',
            name='nomenclaturaDadaPelaAgencia',
            field=models.CharField(max_length=202, verbose_name='Nomenclatura dada pela agencia'),
        ),
        migrations.AlterField(
            model_name='member',
            name='bio',
            field=models.TextField(max_length=211, verbose_name='Biografia'),
        ),
        migrations.AlterField(
            model_name='tipodadopelaagencia',
            name='tipo',
            field=models.CharField(max_length=201, unique=True, verbose_name='Tipo'),
        ),
    ]
