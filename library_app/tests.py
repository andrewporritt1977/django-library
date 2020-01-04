from django.test import SimpleTestCase

# Create your tests here.
class Library_appTests(SimpleTestCase):
    def test_again_page_status_code(self):
        response = self.client.get('again/')
        self.assertEqual(response.status_code, 200)

    def test_test_page_status_code(self):
        response = self.client.get('test/')
        self.assertEqual(response.status_code, 200)