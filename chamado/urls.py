from django.urls import path
from chamado import views

urlpatterns = [
    path('',  views.ChamadoListView.as_view(), name='chamado'),
    path('<str:pk>/', views.chamadoDetail, name='chamado_detail'),
    path('abertura/', views.abreChamado, name='abertura')
]
