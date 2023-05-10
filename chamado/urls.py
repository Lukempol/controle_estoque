from django.urls import path
from chamado import views

urlpatterns = [
    path('',  views.ChamadoListView.as_view(), name='chamado'),
    path('abertura/', views.abreChamado, name='abertura')
]
