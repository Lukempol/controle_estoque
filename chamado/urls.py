from django.urls import path
from django.contrib.auth.decorators import login_required

from chamado import views

urlpatterns = [
    path('',  views.ChamadoListView.as_view(), name='chamado'),
    path('abertura/',login_required(views.abreChamado), name='abertura'),
    path('<str:pk>/', views.chamadoDetail, name='chamado_detail'),
]
