# Generated by Django 3.2.9 on 2021-11-13 02:31

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('sigla', models.CharField(max_length=20, verbose_name='Sigla')),
            ],
            options={
                'verbose_name': 'Agencia',
                'verbose_name_plural': 'Agencias',
            },
        ),
        migrations.CreateModel(
            name='CategoriasParticipante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('categoria', models.CharField(max_length=120, verbose_name='Categoria participante')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='ContribuicoesPorParticipante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('pessoaFisica', models.CharField(default='#', max_length=200, verbose_name='Nome das pessoas fisicas')),
                ('linkContribuicao', models.CharField(max_length=200, verbose_name='Link das contribuições')),
                ('linkResultado', models.CharField(default='#', max_length=200, verbose_name='Link para os resultados')),
                ('linkAnexo', models.CharField(default='#', max_length=200, verbose_name='Link para o anexo')),
                ('pontosDeAtencao', models.TextField(verbose_name='Pontos de atenção')),
            ],
            options={
                'verbose_name': 'ContribuicaoPorParticipante',
                'verbose_name_plural': 'ContribuicoesPorParticipante',
            },
        ),
        migrations.CreateModel(
            name='IndexacaoTema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('indexacaoTema', models.CharField(max_length=10, verbose_name='Indexacao tema')),
            ],
            options={
                'verbose_name': 'indexacaoTema',
                'verbose_name_plural': 'indexacoesTema',
            },
        ),
        migrations.CreateModel(
            name='InstrumentoDeParticipacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('instrumentoDeParticipacao', models.CharField(max_length=100, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Instrumento',
                'verbose_name_plural': 'Instrumentos',
            },
        ),
        migrations.CreateModel(
            name='Monitoracao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('monitorar', models.CharField(max_length=10, verbose_name='Monitorar')),
            ],
            options={
                'verbose_name': 'Monitorar',
                'verbose_name_plural': 'Monitoracoes',
            },
        ),
        migrations.CreateModel(
            name='ObjetivoParticipacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('objetivo', models.TextField(verbose_name='Objetivo')),
            ],
            options={
                'verbose_name': 'Objetivo',
                'verbose_name_plural': 'Objetivos',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('role', models.CharField(max_length=100, verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='SubCategoriasParticipante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('subCategoria', models.CharField(max_length=120, verbose_name='Sub categoria participante')),
            ],
            options={
                'verbose_name': 'Subcategoria',
                'verbose_name_plural': 'Subcategorias',
            },
        ),
        migrations.CreateModel(
            name='SubSubCategoriasParticipante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('subSubCategoria', models.CharField(max_length=120, verbose_name='Sub sub categoria participante')),
            ],
            options={
                'verbose_name': 'SubSubCategoria',
                'verbose_name_plural': 'SubSubCategorias',
            },
        ),
        migrations.CreateModel(
            name='SubSubSubCategoriasParticipante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('subSubSubCategoria', models.CharField(max_length=120, verbose_name='Sub sub sub categoria participante')),
            ],
            options={
                'verbose_name': 'SubSubSubCategoria',
                'verbose_name_plural': 'SubSubSubCategorias',
            },
        ),
        migrations.CreateModel(
            name='TipoDadoPelaAgencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('tipo', models.CharField(max_length=200, verbose_name='Tipo')),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
            },
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('tipoDocumento', models.CharField(max_length=100, verbose_name='Tipo do documento')),
            ],
            options={
                'verbose_name': 'TipoDocumento',
                'verbose_name_plural': 'TiposDocumento',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('bio', models.TextField(max_length=200, verbose_name='Biografia')),
                ('image', stdimage.models.StdImageField(upload_to='team', verbose_name='Imagem')),
                ('facebook', models.CharField(default='#', max_length=100, verbose_name='Facebook')),
                ('twitter', models.CharField(default='#', max_length=100, verbose_name='Twitter')),
                ('instagram', models.CharField(default='#', max_length=100, verbose_name='Instagram')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.role', verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Membro',
                'verbose_name_plural': 'Equipe',
            },
        ),
        migrations.CreateModel(
            name='MecanismoDeParticipacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('temDocumentoConvocacao', models.BooleanField(default=False)),
                ('temDocumentoBase', models.BooleanField(default=False)),
                ('temDocumentoSintese', models.BooleanField(default=False)),
                ('temDocumentoRespostaContribuicoes', models.BooleanField(default=False)),
                ('temDocumentoProdutoFinal', models.BooleanField(default=False)),
                ('dataInicialContribuicoes', models.DateField(verbose_name='Data inicial das Contribuições')),
                ('dataFinalContribuicoes', models.DateField(verbose_name='Data final das Contribuições')),
                ('dataConvocacao', models.DateField(verbose_name='Data da Convocação')),
                ('dataUltimaAtualizacao', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('dataProdutoFinal', models.DateField(verbose_name='Data produto final')),
                ('nomenclaturaDadaPelaAgencia', models.CharField(max_length=200, verbose_name='Nomenclatura dada pela agencia')),
                ('ementa', models.TextField(verbose_name='Ementa')),
                ('indexacaoSubtema', models.CharField(max_length=200, verbose_name='Indexação subtema')),
                ('situacao', models.CharField(max_length=20, verbose_name='Situação')),
                ('quantidadeDeParticipantes', models.PositiveIntegerField(verbose_name='Quantidade de participantes')),
                ('produtoFinalOQue', models.TextField(verbose_name='Produto final o que')),
                ('pontosDeAtencao', models.TextField(verbose_name='Pontos de atenção para o regulação em números')),
                ('agencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.agencia', verbose_name='Agencia')),
                ('instrumentoDeParticipacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.instrumentodeparticipacao', verbose_name='Instrumento de participação')),
                ('monitoracao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.monitoracao', verbose_name='Monitorar')),
                ('objetivoParticipacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.objetivoparticipacao', verbose_name='Objetivo da participação')),
                ('tipoDadoPelaAgencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipodadopelaagencia', verbose_name='Tipo dado pela agencia')),
            ],
            options={
                'verbose_name': 'Mecanismo',
                'verbose_name_plural': 'Mecanismos',
            },
        ),
        migrations.CreateModel(
            name='Manifestacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('simImpacto', models.PositiveIntegerField(verbose_name='Sim impacto')),
                ('naoImpacto', models.PositiveIntegerField(verbose_name='Não impacto')),
                ('nAImpacto', models.PositiveIntegerField(verbose_name='N/A impacto')),
                ('nCImpacto', models.PositiveIntegerField(verbose_name='N/C impacto')),
                ('nDImpacto', models.PositiveIntegerField(verbose_name='N/D impacto')),
                ('temDocumento', models.BooleanField(default=False, verbose_name='Tem documento')),
                ('conteudo', models.TextField(verbose_name='Conteudo da contribuicao')),
                ('contribuicoes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.contribuicoesporparticipante', verbose_name='idContribuicoes')),
            ],
            options={
                'verbose_name': 'Manifestacao',
                'verbose_name_plural': 'Manifestacoes',
            },
        ),
        migrations.CreateModel(
            name='IntermediarioTemaMecanismo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('indexacaoTema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.indexacaotema', verbose_name='Indexacao tema')),
                ('mecanismo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.mecanismodeparticipacao', verbose_name='Mecanismo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DocumentoManifestacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('linkDocumento', models.CharField(max_length=200, verbose_name='Link do documento')),
                ('referencia', models.CharField(max_length=200, verbose_name='Referencia')),
                ('manifestacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.manifestacoes', verbose_name='Manifestação')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('linkDocumento', models.CharField(max_length=500, verbose_name='Link do documento')),
                ('dataDocumento', models.DateField(verbose_name='Data do documento')),
                ('mecanismo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.mecanismodeparticipacao', verbose_name='Mecanismo')),
                ('tipoDocumento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipodocumento', verbose_name='Tipo do documento')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contribuinte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Atualização')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome do contribuinte')),
                ('personalidade', models.CharField(max_length=3, verbose_name='Personalidade')),
                ('entidadeRepresentativa', models.BooleanField(verbose_name='Entidade representativa')),
                ('estatal', models.BooleanField(verbose_name='Estatal')),
                ('agencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.agencia', verbose_name='Agencia')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoriasparticipante', verbose_name='Categoria participante')),
                ('subCategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.subcategoriasparticipante', verbose_name='Subcategoria participante')),
                ('subSubCategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.subsubcategoriasparticipante', verbose_name='Sub sub categoria participante')),
                ('subSubSubCategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.subsubsubcategoriasparticipante', verbose_name='Sub sub sub categoria participante')),
            ],
            options={
                'verbose_name': 'Contribuinte',
                'verbose_name_plural': 'Contribuintes',
            },
        ),
        migrations.AddField(
            model_name='contribuicoesporparticipante',
            name='contribuinte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.contribuinte', verbose_name='Contribuinte'),
        ),
        migrations.AddField(
            model_name='contribuicoesporparticipante',
            name='mecanismo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.mecanismodeparticipacao', verbose_name='Mecanismo'),
        ),
    ]