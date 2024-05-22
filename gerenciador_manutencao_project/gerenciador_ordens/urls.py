from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('show-ordem/<int:pk>', views.ordem_detalhe, name='detalhe-ordem'),

]