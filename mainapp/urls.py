from django.urls import path
from . import views

urlpatterns = [
    path('', views.local_list, name='main_menu'),
    path('local/<int:idlocal>', views.local_view, name="local_view"),
    path('local/delete/<int:idlocal>', views.local_delete, name='local_delete'),
    path('localnew/', views.local_new, name="local_new"),
    path('local/edit/<int:idlocal>', views.local_edit, name="local_edit"),

    path('irmaos/', views.irmaos_list, name='irmaos_view'),
    path('irmao/<int:idirmao>', views.irmaos_view, name="irmao_id_view"),
    path('irmao/delete/<int:idirmao>', views.irmao_delete, name='irmao_delete'),
    path('irmaonew/', views.irmao_new, name="irmao_new"),
    path('irmao/edit/<int:idirmao>', views.irmao_edit, name="irmao_edit"),

    path('distancias/', views.distancias, name='distancias'),

    path('teste/', views.teste, name='teste')
]
