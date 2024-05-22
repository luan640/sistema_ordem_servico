from django.contrib import admin

from .models import Setor,MaquinaSolda,Maquina,Solicitantes,Operador,Ordens,AreaManutencao,TipoManutencao

admin.site.register(Setor)
admin.site.register(MaquinaSolda)
admin.site.register(Maquina)
admin.site.register(Solicitantes)
admin.site.register(Operador)
admin.site.register(Ordens)
admin.site.register(AreaManutencao)
admin.site.register(TipoManutencao)