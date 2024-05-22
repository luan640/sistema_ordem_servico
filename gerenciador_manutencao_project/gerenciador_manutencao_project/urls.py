from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('home/', include('gerenciador_ordens.urls')),
    path('ordem/', include('execucoes.urls')),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
