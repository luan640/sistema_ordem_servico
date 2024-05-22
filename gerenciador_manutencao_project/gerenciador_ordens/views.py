from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.admin.models import LogEntry
from django.db.models import F, ExpressionWrapper, DurationField, Sum

from django.utils import timezone

from .models import Ordens
from gerenciador_ordens.models import Execucao

from datetime import timedelta

def index(request):

    ordem = Ordens.objects.all()

    return render(request, 'home/home.html', {
        'ordem': ordem
    })


def ordem_detalhe(request, pk):

    # Queries    
    ordem = get_object_or_404(Ordens, pk=pk)
    execucoes = Execucao.objects.filter(id_ordem_id=pk).order_by('-n_execucao')
    ultima_execucao = Execucao.objects.filter(id_ordem_id=pk).last()
    primeira_execucao = Execucao.objects.filter(id_ordem_id=pk).first()

    # Calcula o tempo total de execução para cada execução
    for execucao in execucoes:
        execucao.tempo_total = execucao.data_hora_fim - execucao.data_hora_inicio
    
    # Tempo total de ordem de serviço 
    data_abertura_ordem = ordem.data_hora_abertura

    if ultima_execucao.status == 'finalizada':
        data_ultima_execucao = ultima_execucao.data_hora_fim
        tempo_total_ordem_aberta =  data_ultima_execucao - data_abertura_ordem
    else:
        tempo_total_ordem_aberta = timezone.now() - data_abertura_ordem

    # Tempo total de execução com a máquina parada
    tempo_total_exec_maq_parada = (
        Execucao.objects
        .filter(id_ordem_id=pk, exec_maq_parada=1)
        .annotate(diferenca_tempo=ExpressionWrapper(
            F('data_hora_fim') - F('data_hora_inicio'),
            output_field=DurationField()
        ))
        .aggregate(tempo_total=Sum('diferenca_tempo'))
    )

    # Tempo de máquina parada desde que foi aberta a ordem
    if primeira_execucao.maquina_parada:
        tempo_total_maq_parada = ultima_execucao.data_hora_fim - data_abertura_ordem
    else:
        tempo_total_maq_parada = '00:00:00'

    return render(request, 'ordens/detail_ordem.html', {
        'ordem': ordem,
        'execucoes': execucoes,
        'ultima_execucao': ultima_execucao,
        'tempo_total_ordem_aberta': tempo_total_ordem_aberta,
        'tempo_total_exec_maq_parada': tempo_total_exec_maq_parada,
        'tempo_total_maq_parada': tempo_total_maq_parada
    })

