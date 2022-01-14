from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Member
from .forms import ContactForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['team'] = Member.objects.all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar o e-mail! :(')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)


class Error404View(TemplateView):
    template_name = '404.html'


class Error500View(TemplateView):
    template_name = '500.html'


class CsvUploadView(FormView):
    template_name = 'change_list.html'

    def get_context_data(self, **kwargs):
        context = super(CsvUploadView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form, *args, **kwargs):
        messages.success(self.request, 'CSV salvo com sucesso!')
        return super(CsvUploadView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar salvar o CSV! :(')
        return super(CsvUploadView, self).form_invalid(form, *args, **kwargs)