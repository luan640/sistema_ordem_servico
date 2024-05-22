from django.shortcuts import render,redirect

from gerenciador_ordens.models import Execucao
from .forms import AddExecucaoForm

def execucao_add(request,pk):
    
    if request.method == 'POST':
        form = AddExecucaoForm(request.POST)
        
        if form.is_valid():
            # execucao = Execucao.objects.filter(id_ordem_id=pk)[0]

            client = form.save(commit=False)
            client.save()

            return redirect('clients:list')
        
    else:
        form = AddExecucaoForm()

    return render(request, 'add_execucao/add_execucao.html', {
        'form': form,
    })