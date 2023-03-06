from django.urls import path
from produto import views

urlpatterns = [
    path('', views.ProdutoListView.as_view(), name='produto_list'),
    path('<int:pk>/', views.ProdutoDetail, name='produto_detail'),
    path('adicionar', views.CreateProduto.as_view(), name='adicionar'),
]
