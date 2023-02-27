from django.urls import path
from produto import views

urlpatterns = [
    path('', views.ProdutoView.as_view(), name='produto'),
]
