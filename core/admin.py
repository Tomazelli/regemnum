from django.contrib import admin

from .models import Agencia, ObjetivoParticipacao, TipoDadoPelaAgencia, InstrumentoDeParticipacao, Monitoracao
from .models import MecanismoDeParticipacao, IndexacaoTema, IntermediarioTemaMecanismo, TipoDocumento, Documento
from .models import CategoriasParticipante, SubCategoriasParticipante, SubSubCategoriasParticipante
from .models import SubSubSubCategoriasParticipante, Contribuinte, ContribuicoesPorParticipante, Manifestacoes
from .models import DocumentoManifestacao, Role, Member


@admin.register(Agencia)
class AgenciaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla', 'modified')


@admin.register(ObjetivoParticipacao)
class ObjetivoParticipacaoAdmin(admin.ModelAdmin):
    list_display = ('objetivo', 'modified')


@admin.register(TipoDadoPelaAgencia)
class TipoDadoPelaAgenciaAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'modified')


@admin.register(InstrumentoDeParticipacao)
class InstrumentoDeParticipacaoAdmin(admin.ModelAdmin):
    list_display = ('instrumentoDeParticipacao', 'modified')


@admin.register(Monitoracao)
class MonitoracaoAdmin(admin.ModelAdmin):
    list_display = ('monitorar', 'modified')


@admin.register(MecanismoDeParticipacao)
class MecanismoDeParticipacaoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'agencia', 'objetivoParticipacao', 'tipoDadoPelaAgencia', 'instrumentoDeParticipacao', 'modified')


@admin.register(IndexacaoTema)
class IndexacaoTemaAdmin(admin.ModelAdmin):
    list_display = ('indexacaoTema', 'modified')


@admin.register(IntermediarioTemaMecanismo)
class IntermediarioTemaMecanismoAdmin(admin.ModelAdmin):
    list_display = ('mecanismo', 'indexacaoTema', 'modified')


@admin.register(TipoDocumento)
class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = ('tipoDocumento', 'modified')


@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'tipoDocumento', 'mecanismo', 'modified')


@admin.register(CategoriasParticipante)
class CategoriasParticipanteAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'modified')


@admin.register(SubCategoriasParticipante)
class SubCategoriasParticipanteAdmin(admin.ModelAdmin):
    list_display = ('subCategoria', 'modified')


@admin.register(SubSubCategoriasParticipante)
class SubSubCategoriasParticipanteAdmin(admin.ModelAdmin):
    list_display = ('subSubCategoria', 'modified')


@admin.register(SubSubSubCategoriasParticipante)
class SubSubSubCategoriasParticipanteAdmin(admin.ModelAdmin):
    list_display = ('subSubSubCategoria', 'modified')


@admin.register(Contribuinte)
class ContribuinteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'modified')


@admin.register(ContribuicoesPorParticipante)
class ContribuicoesPorParticipanteAdmin(admin.ModelAdmin):
    list_display = ('pk', 'mecanismo', 'contribuinte', 'modified')


@admin.register(Manifestacoes)
class ManifestacoesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'contribuicoes', 'modified')


@admin.register(DocumentoManifestacao)
class DocumentoManifestacaoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'manifestacao', 'modified')


#
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('role', 'modified', 'active')


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'bio', 'modified', 'active')