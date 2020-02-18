from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_menu, name='main_menu'),
    path('local/<int:idlocal>', views.local_view, name="local_view"),
    path('irmaos/', views.irmaos_view, name='irmaos_view'),
    path('irmao/<int:idirmao>', views.irmaos_id_view, name="irmao_id_view"),
    path('distancias/', views.distancias, name='distancias'),
    path('teste/', views.teste, name='teste'),
    path('local/delete/<int:idlocal>', views.local_delete, name='local_delete'),
    path('localnew/', views.local_new, name="local_new"),
    path('local/edit/<int:idlocal>', views.local_edit, name="local_edit")
]
