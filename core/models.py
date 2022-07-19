import uuid
from django.db import models
from stdimage.models import StdImageField

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    
    return filename

class Base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
        #Servem pra selecionar os icones qe serão usados
    )
    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
    def __str__(self):
        return self.servico

class Feature(Base):
    ICONES_CHOICES = (
        ('lni-rocket', 'Foguete'),
        ('lni-laptop-phone', 'Responsividade'),
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-layers', 'Design'),
        ('lni-leaf', 'Sustentabilidade'),
        #ESCOLHER ENTRE OS ÍCONES DISPONÍVEIS
    )
    feature = models.CharField('Feature', max_length=100)
    descricao = models.CharField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=16, choices=ICONES_CHOICES)

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'
    def __str__(self):
        return self.feature

class Plano(Base):
    ICONES_CHOICES = (
        ('lni-package', 'Caixa'),
        ('lni-drop', 'Gota'),
        ('lni-star', 'Estrela'),
    )
    PAGAMENTO_CHOICES = (
        ('sem', 'Semanalmente'),
        ('mês', 'Mensalmente'),
        ('ano', 'Anualmente'),
    )
    plano = models.CharField('Plano', max_length=30)
    preco = models.DecimalField('Preço (R$)', decimal_places=2, max_digits=6, default=0.00)
    pagamento = models.CharField('Pagamento', max_length=3, choices=PAGAMENTO_CHOICES, default='mês')
    usuarios = models.CharField('Usuários', max_length=50)
    armazenamento = models.CharField('Armazenamento', max_length=50)
    suporte = models.CharField('Suporte', max_length=50)
    atualizacoes = models.CharField('Atualizações', max_length=50)
    icone = models.CharField('Icone', max_length=11, choices=ICONES_CHOICES, default='lni-package')

    class Meta:
        verbose_name = 'Plano'
        verbose_name_plural = 'Planos'
    
    def __str__(self):
        return self.plano
    

class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
    
    def __str__(self):
        return self.cargo

class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb' : {'width' : 480, 'height' : 480, 'crop' : True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome