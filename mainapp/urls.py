from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_menu, name='main_menu'),
    path('local/<int:idlocal>', views.local_view, name="local_view"),
    path('irmaos/', views.irmaos_view, name='irmaos_view')
]
