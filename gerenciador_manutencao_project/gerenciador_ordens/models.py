from django.db import models

# Create your models here.

from abertura_ordem.models import Ordens,Operador,TipoManutencao,AreaManutencao


class Execucao(models.Model):
    
    TIPO_STATUS = (
        ('execucao', 'Em execução'),
        ('andamento', 'Em andamento'),
        ('finalizada', 'Finalizada'),
        ('aguardando', 'Aguardando material'),
    )

    id_ordem = models.ForeignKey(Ordens, related_name='execucao_id_ordem', on_delete=models.DO_NOTHING)
    n_execucao = models.IntegerField(blank=True, null=True)
    tipo_manutencao = models.ForeignKey(TipoManutencao, related_name='execucao_tipo_manutencao',on_delete=models.DO_NOTHING)
    area_manutencao = models.ForeignKey(AreaManutencao, related_name='execucao_area_manutencao',on_delete=models.DO_NOTHING)
    data_hora_inicio = models.DateTimeField()
    data_hora_fim = models.DateTimeField()
    operadores = models.ManyToManyField(Operador, related_name='execucao_operador')
    obs_manutencao = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=20, choices=TIPO_STATUS)
    maquina_parada = models.BooleanField(default=False) #ao chegar a máquina estava parada?
    exec_maq_parada = models.BooleanField(default=False) #execução feita com máquina parada?
    # apos_exec_maq_parada = models.BooleanField(default=False) #execução feita com máquina parada?

    class Meta:
        unique_together = ('id_ordem', 'n_execucao')

    def save(self, *args, **kwargs):
        if not self.pk:  # Verifica se é uma nova instância (não está sendo atualizada)
            # Obter o número de execução mais alto para esta ordem
            max_n_execucao = Execucao.objects.filter(id_ordem=self.id_ordem).aggregate(models.Max('n_execucao'))['n_execucao__max']
            # Se houver execuções anteriores, incrementar o número de execução, caso contrário, definir como 1
            self.n_execucao = max_n_execucao + 1 if max_n_execucao is not None else 1
        super().save(*args, **kwargs)

