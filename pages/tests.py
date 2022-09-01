from django.test import SimpleTestCase, TestCase
from .models import Post

class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(id= 1, title='just a test')
    
    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.title}'
        self.assertEqual(expected_object_name, 'just a test')

class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(title='this is another test')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)


class SimpleTests(SimpleTestCase):
    
    def test_about_us_status_code(self):
        response = self.client.get('/aboutus/')
        self.assertEqual(response.status_code, 200)
