from django.db import models
from django.contrib.auth import get_user_model  # para usar o usuário do django como foreign key


class Local(models.Model):
    opcoesstatus = (
        ('A', 'Assembléia'),
        ('I', 'Informal'),
    )
    nomelocal = models.CharField(max_length=50)
    statuslocal = models.CharField(max_length=1, choices=opcoesstatus, default='A')
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    dataini = models.DateField(null=True, blank=True)
    irmaocontato = models.CharField(max_length=50, null=True, blank=True)
    telefonecontato = models.CharField(max_length=12, null=True, blank=True)
    usuario = models.ForeignKey(get_user_model(), default='admin', on_delete=models.DO_NOTHING)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Locais'

    def __str__(self):
        return self.nomelocal


class Irmao(models.Model):
    opcoescontato = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )
    opcoesuf = (
        ('SP', 'São Paulo'),
        ('MG', 'Minas Gerais'),
        ('RJ', 'Rio de Janeiro'),
    )
    opcoesgenero = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
    )
    opcoesstatus = (
        ('CAT', 'Comunhão Ativo'),
        ('CAU', 'Comunhão Ausente'),
        ('DIS', 'Disciplina'),
        ('VIS', 'Visitante'),
        ('PEL', 'Pediu Lugar a Mesa')
    )
    opcoes_estado_civil = (
        ('CAS', 'Casado'),
        ('SOL', 'Solteiro'),
        ('DIV', 'Divorciado'),
        ('SEP', 'Separado'),
        ('VIU', 'Viúvo')
    )
    nome = models.CharField(max_length=100)
    local = models.ForeignKey(Local, on_delete=models.DO_NOTHING)
    contatolocal = models.CharField(max_length=1, choices=opcoescontato, default='N')
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2, choices=opcoesuf)
    genero = models.CharField(max_length=1, choices=opcoesgenero)
    datanasc = models.DateField(null=True, blank=True)
    estadocivil = models.CharField(max_length=20, choices=opcoes_estado_civil, null=True, blank=True)
    telefonecontato = models.CharField(max_length=12, null=True, blank=True)
    parentes = models.TextField(max_length=100, null=True, blank=True)
    fotolink = models.CharField(max_length=100, null=True, blank=True)
    observacoes = models.TextField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=3, choices=opcoesstatus)
    usuario = models.ForeignKey(get_user_model(), default='admin', on_delete=models.DO_NOTHING)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Irmaos'

    def __str__(self):
        return self.nome
