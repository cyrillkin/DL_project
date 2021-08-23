from django.test import Client, TestCase
from django.urls import reverse


class TestCoreViews(TestCase):

    def setUp(self):
        self.client = Client()
        return super().setUp()

    def test_index_view(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_edit_profile_view(self):
        response = self.client.get(reverse('root:profile-edit', args=(1, )))
        self.assertEqual(response.status_code, 404)

    def test_edit_content(self):
        client = Client()
        response = client.get('/')
        self.assertContains(response, 'РАЗДЕЛЫ')
