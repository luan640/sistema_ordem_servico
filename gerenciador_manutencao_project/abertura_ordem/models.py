from django.db import models

# Create your models here.

class Setor(models.Model):
    
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class MaquinaSolda(models.Model):
    
    nome = models.CharField(max_length=200)
    setor = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.nome} - {self.setor}'


class TipoManutencao(models.Model):

    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class AreaManutencao(models.Model):

    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Solicitantes(models.Model):
    
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=200)
    setor = models.ForeignKey(Setor, related_name='solicitante_setor', on_delete=models.DO_NOTHING)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.matricula} - {self.nome}'

class Operador(models.Model):
    
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=200)
    salario = models.FloatField(null=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.matricula} - {self.nome} - {self.salario}'

class Maquina(models.Model):
    
    nome = models.CharField(max_length=100)
    codigo = models.CharField(primary_key=True, max_length=200)
    tombamento = models.CharField(max_length=200)
    apelido = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    setor = models.ForeignKey(Setor, related_name='maquina_setor', on_delete=models.DO_NOTHING)
    setor_maquina_solda = models.ForeignKey(MaquinaSolda, related_name='maquina_setor_solda', on_delete=models.DO_NOTHING, blank=True, null=True)
    # qual ferramenta
    # codigo da ferramenta


    def __str__(self):
        return self.nome

class Ordens(models.Model):

    OPCAO_IMPACTO_PRODUCAO = (
        ('alto', 'Alto'),
        ('baixo', 'Baixo'),
        ('medio', 'Médio'),
    )
    
    solicitante = models.ForeignKey(Solicitantes, related_name='ordens_solicitantes', on_delete=models.DO_NOTHING)
    setor = models.ForeignKey(Setor, related_name='ordens_setor' ,on_delete=models.DO_NOTHING)
    maquina = models.ForeignKey(Maquina, related_name='ordens_maquina' ,on_delete=models.DO_NOTHING)
    local_maquina = models.CharField(max_length=200, null=True)
    setor_maquina_solda = models.ForeignKey(MaquinaSolda, related_name='ordens_maquina_solda', on_delete=models.DO_NOTHING, null=True)
    descricao = models.CharField(max_length=200)
    impacto_producao = models.CharField(max_length=20, choices=OPCAO_IMPACTO_PRODUCAO)
    maquina_parada = models.BooleanField(default=False)
    data_hora_abertura = models.DateTimeField(auto_now_add=True)
    foto = models.ImageField(upload_to='photo/', null=True)
    video = models.ImageField(upload_to='video/', null=True)