from django.urls import path

from . import views

urlpatterns = [
    path('executar-ordem/<int:pk>', views.execucao_add, name='executar-ordem'),

]