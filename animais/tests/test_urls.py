from urllib import request
from django.test import TestCase, RequestFactory
from django.urls import reverse
from animais.views import index


class AnimaisURLSTestCase(TestCase):
    """Teste se a home esta utilizando"""
    def setUp(self):
        self.factory = RequestFactory()

    def test_rota_url_utiliza_view_index(self):
        request = self.factory.get('/')
        with self.assertTemplateUsed('index.html'):
            response = index(request)
            self.assertEqual(response.status_code, 200)
            