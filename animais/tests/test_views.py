from urllib import response
from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet
from animais.models import Animal


class IndexViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.animal = Animal.objects.create(
            nome_animal = 'calopsita',
            predador = 'Não',
            venenoso = 'Não',
            domestico = 'Sim'
        )
    
    def test_index_view_retorna_caracteristicas_animal(self):
        response = self.client.get('/',
            {'buscar': 'calopsita'}
        )
        animal_pesquisado = response.context['caracteriticas']
        self.assertIs(type(response.context['caracteriticas']), QuerySet)
        self.assertEqual(animal_pesquisado[0].nome_animal, 'calopsita')
