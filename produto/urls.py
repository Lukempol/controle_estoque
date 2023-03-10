from django.urls import path
from produto import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.ProdutoListView.as_view(), name='produto_list'),
    path('<int:pk>/', views.ProdutoDetail, name='produto_detail'),
    path('adicionar/', login_required(views.CreateProduto.as_view()), name='adicionar'),
    path('editar/<int:pk>/', login_required(views.EditProduto.as_view()), name='editar'),
    path('deletar/<int:pk>/', login_required(views.DeleteProduto.as_view()), name='deletar'),
    path('relatorio/', views.some_view, name='relatorio'),
]
