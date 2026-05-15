from django.test import TestCase, Client
from .models import KebabShop
import json


class KebabShopAPITest(TestCase):
    def setUp(self):
        self.client = Client()
        self.k1 = KebabShop.objects.create(
            name='Test Kebab',
            address='Main St 1',
            city='Prague',
            opening_hours='9-21',
            email='test@example.com',
            meat_type='lamb'
        )

    def test_list_kebabshops(self):
        resp = self.client.get('/api/kebabshop')
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.content)
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 1)

    def test_get_kebabshop_detail(self):
        resp = self.client.get(f'/api/kebabshop/{self.k1.id}')
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.content)
        self.assertEqual(data['id'], self.k1.id)
        self.assertEqual(data['name'], self.k1.name)

    def test_create_kebabshop(self):
        payload = {
            'name': 'New Kebab',
            'address': 'New St 2',
            'city': 'Brno',
            'opening_hours': '10-22',
            'email': 'new@example.com',
            'meat_type': 'beef'
        }
        resp = self.client.post('/api/kebabshop', json.dumps(payload), content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.content)
        self.assertEqual(data['name'], payload['name'])
        self.assertTrue(KebabShop.objects.filter(id=data['id']).exists())

    def test_update_kebabshop(self):
        payload = {
            'name': 'Updated Kebab',
            'address': 'Updated St',
            'city': 'Ostrava',
            'opening_hours': '11-23',
            'email': 'upd@example.com',
            'meat_type': 'chicken'
        }
        resp = self.client.put(f'/api/kebabshop/{self.k1.id}', json.dumps(payload), content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.content)
        self.assertEqual(data['name'], payload['name'])
        self.k1.refresh_from_db()
        self.assertEqual(self.k1.name, payload['name'])
