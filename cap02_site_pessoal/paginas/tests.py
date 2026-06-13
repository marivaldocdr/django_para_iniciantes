from django.test import SimpleTestCase


# Crie seus testes aqui.
class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/sobre/")
        self.assertEqual(response.status_code, 200)
