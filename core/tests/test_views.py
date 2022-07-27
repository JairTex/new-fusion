from django.test import TestCase, Client
from django.urls import reverse_lazy

class IndexViewtestCase(TestCase):
    
    def setUp(self):
        self.dados = {
            'nome' : 'selfnome',
            'email' : 'selfemail@gmail.com',
            'assunto' : 'selfassunto',
            'mensagem' : 'selfmensagem'
        } #Simulando o JSON recebido no POST

        self.cliente = Client()

    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 302) #Código de redirecionamento

    def test_form_invalid(self):
        dados = {
            'nome' : 'exemplo',
            'assunto' : 'Assunto Teste'
        }
        request = self.cliente.post(reverse_lazy('index'), data=dados)
        self.assertEquals(request.status_code, 200) #Houve algum erro e não fez o redirecionamento
        
