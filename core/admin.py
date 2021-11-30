from django.contrib import admin
from django.db import models
from django.forms import TextInput

from .models import Agencia, ObjetivoParticipacao, TipoDadoPelaAgencia, InstrumentoDeParticipacao, Monitoracao
from .models import MecanismoDeParticipacao, IndexacaoTema, IntermediarioTemaMecanismo, TipoDocumento, Documento
from .models import CategoriasParticipante, SubCategoriasParticipante, SubSubCategoriasParticipante
from .models import SubSubSubCategoriasParticipante, Contribuinte, ContribuicoesPorParticipante, Manifestacoes
from .models import DocumentoManifestacao, Role, Member


@admin.register(Agencia)
class AgenciaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla', 'modified')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
        models.IntegerField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vIntegerField'})},
        models.URLField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vURLField'})},
    }


@admin.register(ObjetivoParticipacao)
class ObjetivoParticipacaoAdmin(admin.ModelAdmin):
    list_display = ('objetivo', 'modified')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
        models.IntegerField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vIntegerField'})},
        models.URLField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vURLField'})},
    }


@admin.register(TipoDadoPelaAgencia)
class TipoDadoPelaAgenciaAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'modified')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
        models.IntegerField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vIntegerField'})},
        models.URLField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vURLField'})},
    }


@admin.register(InstrumentoDeParticipacao)
class InstrumentoDeParticipacaoAdmin(admin.ModelAdmin):
    list_display = ('instrumentoDeParticipacao', 'modified')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
        models.IntegerField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vIntegerField'})},
        models.URLField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vURLField'})},
    }


@admin.register(Monitoracao)
class MonitoracaoAdmin(admin.ModelAdmin):
    list_display = ('monitorar', 'modified')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
        models.IntegerField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vIntegerField'})},
        models.URLField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vURLField'})},
    }


@admin.register(MecanismoDeParticipacao)
class MecanismoDeParticipacaoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'agencia', 'nomenclaturaDadaPelaAgencia', 'dataInicialContribuicoes', 'modified')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
        models.IntegerField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vIntegerField'})},
        models.URLField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vURLField'})},
    }


@admin.register(IndexacaoTema)
class IndexacaoTemaAdmin(admin.ModelAdmin):
    list_display = ('indexacaoTema', 'modified')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
        models.IntegerField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vIntegerField'})},
        models.URLField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vURLField'})},
    }


@admin.register(IntermediarioTemaMecanismo)
class IntermediarioTemaMecanismoAdmin(admin.ModelAdmin):
    list_display = ('mecanismo', 'indexacaoTema', 'modified')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
        models.IntegerField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vIntegerField'})},
        models.URLField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vURLField'})},
    }


@admin.register(TipoDocumento)
class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = ('tipoDocumento', 'modified')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
        models.IntegerField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vIntegerField'})},
        models.URLField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vURLField'})},
    }


@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'tipoDocumento', 'mecanismo', 'modified')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
        models.IntegerField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vIntegerField'})},
        models.URLField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vURLField'})},
    }


@admin.register(CategoriasParticipante)
class CategoriasParticipanteAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'modified')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
        models.IntegerField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vIntegerField'})},
        models.URLField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vURLField'})},
    }


@admin.register(SubCategoriasParticipante)
class SubCategoriasParticipanteAdmin(admin.ModelAdmin):
    list_display = ('subCategoria', 'modified')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
        models.IntegerField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vIntegerField'})},
        models.URLField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vURLField'})},
    }


@admin.register(SubSubCategoriasParticipante)
class SubSubCategoriasParticipanteAdmin(admin.ModelAdmin):
    list_display = ('subSubCategoria', 'modified')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
        models.IntegerField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vIntegerField'})},
        models.URLField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vURLField'})},
    }


@admin.register(SubSubSubCategoriasParticipante)
class SubSubSubCategoriasParticipanteAdmin(admin.ModelAdmin):
    list_display = ('subSubSubCategoria', 'modified')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
        models.IntegerField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vIntegerField'})},
        models.URLField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vURLField'})},
    }


@admin.register(Contribuinte)
class ContribuinteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'modified')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
        models.IntegerField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vIntegerField'})},
        models.URLField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vURLField'})},
    }


@admin.register(ContribuicoesPorParticipante)
class ContribuicoesPorParticipanteAdmin(admin.ModelAdmin):
    list_display = ('pk', 'mecanismo', 'contribuinte', 'modified')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
        models.IntegerField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vIntegerField'})},
        models.URLField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vURLField'})},
    }


@admin.register(Manifestacoes)
class ManifestacoesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'contribuicoes', 'modified')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
        models.IntegerField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vIntegerField'})},
        models.URLField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vURLField'})},
    }


@admin.register(DocumentoManifestacao)
class DocumentoManifestacaoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'manifestacao', 'modified')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
        models.IntegerField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vIntegerField'})},
        models.URLField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vURLField'})},
    }


#
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('role', 'modified', 'active')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
        models.IntegerField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vIntegerField'})},
        models.URLField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vURLField'})},
    }


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'bio', 'modified', 'active')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
        models.IntegerField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vIntegerField'})},
        models.URLField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vURLField'})},
    }