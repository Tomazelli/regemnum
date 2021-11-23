import uuid
from django.db import models

from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    created = models.DateTimeField('Criação', auto_now_add=True)
    modified = models.DateTimeField('Atualização', auto_now=True)
    active = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class Agencia(Base):
    nome = models.CharField('Nome', max_length=200)
    sigla = models.CharField('Sigla', max_length=20)

    class Meta:
        verbose_name = 'Agencia'
        verbose_name_plural = 'Agencias'

    def __str__(self):
        return self.nome


class ObjetivoParticipacao(Base):
    objetivo = models.TextField('Objetivo')

    class Meta:
        verbose_name = 'Objetivo'
        verbose_name_plural = 'Objetivos'

    def __str__(self):
        return self.objetivo


class TipoDadoPelaAgencia(Base):
    tipo = models.CharField('Tipo', max_length=200)

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'

    def __str__(self):
        return self.tipo


class InstrumentoDeParticipacao(Base):
    instrumentoDeParticipacao = models.CharField('Nome', max_length=100)

    class Meta:
        verbose_name = 'Instrumento'
        verbose_name_plural = 'Instrumentos'

    def __str__(self):
        return self.instrumentoDeParticipacao


class Monitoracao(Base):
    monitorar = models.CharField('Monitorar', max_length=10, default='#')

    class Meta:
        verbose_name = 'Monitorar'
        verbose_name_plural = 'Monitoracoes'

    def __str__(self):
        return self.monitorar


class MecanismoDeParticipacao(Base):
    # FK
    objetivoParticipacao = models.ForeignKey(
        'core.ObjetivoParticipacao', verbose_name='Objetivo da participação', on_delete=models.CASCADE)
    agencia = models.ForeignKey(
        'core.Agencia', verbose_name='Agencia', on_delete=models.CASCADE)
    tipoDadoPelaAgencia = models.ForeignKey(
        'core.TipoDadoPelaAgencia', verbose_name='Tipo dado pela agencia', on_delete=models.CASCADE)
    instrumentoDeParticipacao = models.ForeignKey(
        'core.InstrumentoDeParticipacao', verbose_name='Instrumento de participação', on_delete=models.CASCADE)
    monitoracao = models.ForeignKey(
        'core.Monitoracao', verbose_name='Monitorar', on_delete=models.CASCADE)
    #

    # temDocumentos
    temDocumentoConvocacao = models.BooleanField(default=False)
    temDocumentoBase = models.BooleanField(default=False)
    temDocumentoSintese = models.BooleanField(default=False)
    temDocumentoRespostaContribuicoes = models.BooleanField(default=False)
    temDocumentoProdutoFinal = models.BooleanField(default=False)
    #

    # datas
    dataInicialContribuicoes = models.DateField(
        'Data inicial das Contribuições (AAAA-MM-DD)')
    dataFinalContribuicoes = models.DateField(
        'Data final das Contribuições (AAAA-MM-DD)')
    dataConvocacao = models.DateField('Data da Convocação (AAAA-MM-DD)')
    dataUltimaAtualizacao = models.DateField(
        'Atualização (AAAA-MM-DD)', auto_now=True)
    dataProdutoFinal = models.DateField('Data produto final (AAAA-MM-DD)')
    #

    # demais campos
    nomenclaturaDadaPelaAgencia = models.CharField(
        'Nomenclatura dada pela agencia', max_length=200)
    ementa = models.TextField('Ementa')
    indexacaoSubtema = models.CharField('Indexação subtema', max_length=200)
    situacao = models.CharField('Situação', max_length=20)
    quantidadeDeParticipantes = models.PositiveIntegerField(
        'Quantidade de participantes')
    produtoFinalOQue = models.TextField('Produto final o que')
    pontosDeAtencao = models.TextField(
        'Pontos de atenção para o regulação em números')

    class Meta:
        verbose_name = 'Mecanismo'
        verbose_name_plural = 'Mecanismos'

    def __str__(self):
        return self.nomenclaturaDadaPelaAgencia


class IndexacaoTema(Base):
    indexacaoTema = models.CharField('Indexacao tema', max_length=10)

    class Meta:
        verbose_name = 'indexacaoTema'
        verbose_name_plural = 'indexacoesTema'

    def __str__(self):
        return self.indexacaoTema


class IntermediarioTemaMecanismo(Base):
    # FK
    mecanismo = models.ForeignKey(
        'core.MecanismoDeParticipacao', verbose_name='Mecanismo', on_delete=models.CASCADE)
    indexacaoTema = models.ForeignKey(
        'core.IndexacaoTema', verbose_name='Indexacao tema', on_delete=models.CASCADE)
    #


class TipoDocumento(Base):
    tipoDocumento = models.CharField('Tipo do documento', max_length=100)

    class Meta:
        verbose_name = 'TipoDocumento'
        verbose_name_plural = 'TiposDocumento'

    def __str__(self):
        return self.tipoDocumento


class Documento(Base):
    # FK
    mecanismo = models.ForeignKey(
        'core.MecanismoDeParticipacao', verbose_name='Mecanismo', on_delete=models.CASCADE)
    tipoDocumento = models.ForeignKey(
        'core.TipoDocumento', verbose_name='Tipo do documento', on_delete=models.CASCADE)
    #

    # demais campos
    linkDocumento = models.CharField('Link do documento', max_length=500)
    dataDocumento = models.DateField('Data do documento')
    #


class CategoriasParticipante(Base):
    categoria = models.CharField('Categoria participante', max_length=120)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.categoria


class SubCategoriasParticipante(Base):
    subCategoria = models.CharField(
        'Sub categoria participante', max_length=120)

    class Meta:
        verbose_name = 'Subcategoria'
        verbose_name_plural = 'Subcategorias'

    def __str__(self):
        return self.subCategoria


class SubSubCategoriasParticipante(Base):
    subSubCategoria = models.CharField(
        'Sub sub categoria participante', max_length=120)

    class Meta:
        verbose_name = 'SubSubCategoria'
        verbose_name_plural = 'SubSubCategorias'

    def __str__(self):
        return self.subSubCategoria


class SubSubSubCategoriasParticipante(Base):
    subSubSubCategoria = models.CharField(
        'Sub sub sub categoria participante', max_length=120)

    class Meta:
        verbose_name = 'SubSubSubCategoria'
        verbose_name_plural = 'SubSubSubCategorias'

    def __str__(self):
        return self.subSubSubCategoria


class Contribuinte(Base):
    # FK
    categoria = models.ForeignKey('core.CategoriasParticipante',
                                  verbose_name='Categoria participante', on_delete=models.CASCADE)
    subCategoria = models.ForeignKey('core.SubCategoriasParticipante',
                                     verbose_name='Subcategoria participante', on_delete=models.CASCADE)
    subSubCategoria = models.ForeignKey('core.SubSubCategoriasParticipante',
                                        verbose_name='Sub sub categoria participante', on_delete=models.CASCADE)
    subSubSubCategoria = models.ForeignKey('core.SubSubSubCategoriasParticipante',
                                           verbose_name='Sub sub sub categoria participante', on_delete=models.CASCADE)
    agencia = models.ForeignKey(
        'core.Agencia', verbose_name='Agencia', on_delete=models.CASCADE)
    #

    nome = models.CharField('Nome do contribuinte', max_length=200)
    personalidade = models.CharField('Personalidade', max_length=3)
    entidadeRepresentativa = models.BooleanField('Entidade representativa')
    estatal = models.BooleanField('Estatal')

    class Meta:
        verbose_name = 'Contribuinte'
        verbose_name_plural = 'Contribuintes'

    def __str__(self):
        return self.nome


class ContribuicoesPorParticipante(Base):
    # FK
    mecanismo = models.ForeignKey(
        'core.MecanismoDeParticipacao', verbose_name='Mecanismo', on_delete=models.CASCADE)
    contribuinte = models.ForeignKey(
        'core.Contribuinte', verbose_name='Contribuinte', on_delete=models.CASCADE)
    #

    # demais campos
    pessoaFisica = models.CharField(
        'Nome das pessoas fisicas', max_length=200, default='#')
    linkContribuicao = models.CharField(
        'Link das contribuições', max_length=200)
    linkResultado = models.CharField(
        'Link para os resultados', max_length=200, default='#')
    linkAnexo = models.CharField(
        'Link para o anexo', max_length=200, default='#')
    pontosDeAtencao = models.TextField('Pontos de atenção', default='#')
    #

    class Meta:
        verbose_name = 'ContribuicaoPorParticipante'
        verbose_name_plural = '>>Comece preenchendo por aqui!<<'

    def __str__(self):
        return str(self.pk)


class Manifestacoes(Base):
    # FK
    contribuicoes = models.ForeignKey(
        'core.ContribuicoesPorParticipante', verbose_name='idContribuicoes', on_delete=models.CASCADE)
    #

    # demais campos
    simImpacto = models.PositiveIntegerField('Sim impacto')
    naoImpacto = models.PositiveIntegerField('Não impacto')
    nAImpacto = models.PositiveIntegerField('N/A impacto')
    nCImpacto = models.PositiveIntegerField('N/C impacto')
    nDImpacto = models.PositiveIntegerField('N/D impacto')
    temDocumento = models.BooleanField('Tem documento', default=False)
    conteudo = models.TextField('Conteudo da contribuicao', default='#')
    #

    class Meta:
        verbose_name = 'Manifestacao'
        verbose_name_plural = 'Manifestacoes'

    def __str__(self):
        return str(self.pk)


class DocumentoManifestacao(Base):
    # FK
    manifestacao = models.ForeignKey(
        'core.Manifestacoes', verbose_name='Manifestação', on_delete=models.CASCADE)
    #

    linkDocumento = models.CharField('Link do documento', max_length=200)
    referencia = models.CharField('Referencia', max_length=200)


#
#
#
class Role(Base):
    role = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.role


class Member(Base):
    name = models.CharField('Nome', max_length=100)
    role = models.ForeignKey(
        'core.Role', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Biografia', max_length=200)
    #image = StdImageField('Imagem', upload_to='team', variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    image = models.CharField('Imagem', max_length=100)
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Membro'
        verbose_name_plural = 'Equipe'

    def __str__(self):
        return self.name
