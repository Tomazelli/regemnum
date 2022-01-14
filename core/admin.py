import datetime
import csv

from django.contrib import admin, messages
from django.db import models
from django.forms import TextInput
from django.urls import path, reverse
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect

import core.models
from .models import Agencia, ObjetivoParticipacao, TipoDadoPelaAgencia, InstrumentoDeParticipacao, Monitoracao
from .models import MecanismoDeParticipacao, IndexacaoTema, IntermediarioTemaMecanismo, TipoDocumento, Documento
from .models import CategoriasParticipante, SubCategoriasParticipante, SubSubCategoriasParticipante
from .models import SubSubSubCategoriasParticipante, Contribuinte, ContribuicoesPorParticipante, Manifestacoes
from .models import DocumentoManifestacao, Role, Member


class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()


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

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv), ]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]

            if not csv_file.name.endswith('.csv'):
                messages.warning(request, "O arquivo não é um csv!")
                return HttpResponseRedirect(request.path_info)

            file_data = csv_file.read().decode("utf-8")

            csv_data = []
            csv_data_temp = []

            text = ''
            firstQuote = False
            secondQuote = False
            for x in file_data:
                for char in x:
                    # removendo a quebra de linha de separação
                    if char != '\n':
                        if char != '\r':
                            text = text + char

                    # colocando quebras de linha de strings
                    if firstQuote:
                        if (char == '\n') or (char == '\r'):
                            text = text + char

                    # tratando strings que contém virgula
                    if char == '\"':
                        if firstQuote:
                            secondQuote = True
                        firstQuote = True
                        if secondQuote:
                            firstQuote = False
                            secondQuote = False

                    # adicionando o campo
                    if not firstQuote:
                        if char == '\n':
                            csv_data_temp.append(text)
                            text = ''
                if csv_data_temp:
                    csv_data.append(csv_data_temp)
                csv_data_temp = []

            fields = []
            fieldsTemp = []

            # pegando os campos do csv
            text = ''
            firstQuote = False
            secondQuote = False
            for x in csv_data:
                for y in x:
                    for char in y:
                        # removendo a virgulas de separação
                        if char != ',':
                            text = text + char

                        # colocando virgulas de strings
                        if firstQuote:
                            if char == ',':
                                text = text + char

                        # tratando strings que contém virgula
                        if char == '\"':
                            if firstQuote:
                                secondQuote = True
                            firstQuote = True
                            if secondQuote:
                                firstQuote = False
                                secondQuote = False

                        # adicionando o campo
                        if not firstQuote:
                            if char == ',':
                                fieldsTemp.append(text)
                                text = ''
                fields.append(fieldsTemp)
                fieldsTemp = []

            # salvando o nome dos campos
            csv_labels = fields.pop(0)

            csv_label_index_dict = {}

            # criando dicionario para identificar os indexes pelo nome dos campos
            i = 0
            for x in csv_labels:
                csv_label_index_dict[x] = i
                i = i + 1

            ## pequena funcao para converter strings especificas em boolean
            def checkBoolean(value):
                if value == "Disponível":
                    return True
                else:
                    return False

            ## pequena funcao para concertar datas nao especificadas
            def checkDate(value):
                if len(value) != 10:
                    return "1970/01/01"
                else:
                    return value

            # salvando os campos no banco de dados
            for field in fields:

                created_objetivo = ObjetivoParticipacao.objects.update_or_create(
                    objetivo=field[csv_label_index_dict['Objetivo_participacao']],
                )


                created_tipodadopelaagencia = TipoDadoPelaAgencia.objects.update_or_create(
                    tipo=field[csv_label_index_dict['Nomenclatura_dada_pela_Agencia']],
                )


                created_instrumentodeparticipacao = InstrumentoDeParticipacao.objects.update_or_create(
                    instrumentoDeParticipacao=field[csv_label_index_dict['Instrumento_de_Participacao']],
                )

                print(csv_label_index_dict['Monitorar'])
                print(field)
                created_monitoracao = Monitoracao.objects.update_or_create(
                    monitorar=field[csv_label_index_dict['Monitorar']],
                )


                # print(field)
                # print(csv_labels)
                # print(field[csv_label_index_dict['Quantos_participaram']])
                created_mecanismo = MecanismoDeParticipacao.objects.update_or_create(

                    # FK's
                    objetivoParticipacao=ObjetivoParticipacao.objects.get(
                        objetivo=field[csv_label_index_dict['Objetivo_participacao']]),
                    agencia=Agencia.objects.get(sigla=field[csv_label_index_dict['Agência']]),
                    tipoDadoPelaAgencia=TipoDadoPelaAgencia.objects.get(
                        tipo=field[csv_label_index_dict['Nomenclatura_dada_pela_Agencia']]),
                    instrumentoDeParticipacao=InstrumentoDeParticipacao.objects.get(
                        instrumentoDeParticipacao=field[csv_label_index_dict['Instrumento_de_Participacao']]),
                    monitoracao=Monitoracao.objects.get(monitorar=field[csv_label_index_dict['Monitorar']]),

                    # demais campos

                    temDocumentoConvocacao=checkBoolean(field[csv_label_index_dict['tem_documento_convocacao']]),
                    temDocumentoBase=checkBoolean(field[csv_label_index_dict['tem_documento_base']]),
                    temDocumentoSintese=checkBoolean(field[csv_label_index_dict['tem_documento_síntese_mecanismo']]),
                    temDocumentoRespostaContribuicoes=checkBoolean(field[
                                                                       csv_label_index_dict[
                                                                           'tem_documento_resposta_contribuicoes']]),
                    temDocumentoProdutoFinal=checkBoolean(field[csv_label_index_dict['tem_documento_produto_final']]),

                    dataInicialContribuicoes=datetime.datetime.strptime(
                        checkDate(field[csv_label_index_dict['Contribuicao_data_inicial']]), '%Y/%m/%d'),
                    dataFinalContribuicoes=datetime.datetime.strptime(
                        checkDate(field[csv_label_index_dict['Contribuicao_data_final']]), '%Y/%m/%d'),
                    dataConvocacao=datetime.datetime.strptime(checkDate(field[csv_label_index_dict['Convocacao_Data']]),
                                                              '%Y/%m/%d'),
                    dataProdutoFinal=datetime.datetime.strptime(
                        checkDate(field[csv_label_index_dict['Produto_Final_Data']]), '%Y/%m/%d'),

                    nomenclaturaDadaPelaAgencia=field[csv_label_index_dict['ID_Agencia']],
                    ementa=field[csv_label_index_dict['Ementa']],
                    indexacaoSubtema=field[csv_label_index_dict['Indexacao_Subtema']],
                    situacao=field[csv_label_index_dict['Situacao']],
                    quantidadeDeParticipantes=field[csv_label_index_dict['Quantos_participaram']],
                    produtoFinalOQue=field[csv_label_index_dict['Produto_final_o_que']],
                    pontosDeAtencao=field[csv_label_index_dict['Pontos_de_Atencao_para_o_Regulacao_em_Numeros']],

                )

            return HttpResponseRedirect(reverse('admin:index'))

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)


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
