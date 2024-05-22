from django import forms

from gerenciador_ordens.models import Execucao

class AddExecucaoForm(forms.ModelForm):
    class Meta:
        model = Execucao
        fields = ('data_hora_inicio','data_hora_fim')