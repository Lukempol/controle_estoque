from django.test import TestCase, Client
from produto.models import Produto  

class ProdutoTestCase(TestCase):
    def setUp(self):
        Produto.objects.create(name="Água")
        Produto.objects.create(name="Mesa")
        Produto.objects.create(name="Xadrez")
        return super().setUp()
    
    def test_nome_simples_sem_acento(self):
        obj = Produto.objects.filter(name="Água").first()
        self.assertEqual(obj.simple_name, "agua")
    
    def test_cod_gerado_automaticamente(self):
        obj1 = Produto.objects.filter(name="Xadrez").first()
        obj2 = Produto.objects.filter(name="Xadrez").first()
        obj3 = Produto.objects.filter(name="Xadrez").first()
        assert obj1 is not None
        assert obj2 is not None
        assert obj3 is not None
    
    def test_cod_4_digitos_gerado_automatico(self):
        obj = Produto.objects.filter(name="Água").first()
        self.assertEqual(len(str(obj.cod)), 4)

    def test_detail_view_response_404(self):
        c =Client()
        response1 = c.get('produto/12')
        response2 = c.get('produto/123')
        response3 = c.get('produto/12345')
        response4 = c.get('produto/123456')
        self.assertEqual(response1.status_code, 404)
        self.assertEqual(response2.status_code, 404)
        self.assertEqual(response3.status_code, 404)
        self.assertEqual(response4.status_code, 404)
    
    def test_update_view(self):
        obj = Produto.objects.filter(name="Xadrez").first()
        obj.quantidade = 200
        obj.save()
        obj2 = Produto.objects.filter(name="Xadrez").first()
        self.assertEqual(obj2.quantidade, 200)

    def test_delete_veiw(self):
        c = Client()
        obj = Produto.objects.filter(name="Mesa").first()
        c.get('delete/'+str(obj.cod))
        response = c.get('produto/'+str(obj.cod))
        self.assertEqual(response.status_code, 404)