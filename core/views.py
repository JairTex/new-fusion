from django.urls import reverse_lazy
from django.views.generic import FormView
from .models import Servico, Funcionario, Feature, Plano
from .forms import ContatoForm
from django.contrib import messages

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        
        context['servicos'] = Servico.objects.order_by('?').all()

        context['features1'] = Feature.objects.all()[:3]
        context['features2'] = Feature.objects.all()[3:6]

        context['planos'] = Plano.objects.all()

        context['funcionarios'] = Funcionario.objects.order_by('nome').all()
        
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro no envio do e-mail!')

        return super(IndexView, self).form_invalid(form, *args, **kwargs)
