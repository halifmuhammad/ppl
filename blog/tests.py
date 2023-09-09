from django.test import TestCase
from .models import Post

# Create your tests here.
class ModelTesting(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title='test post', author='test', message='test message')
    
    def test_post_model(self):
        post = self.post
        self.assertTrue(isinstance(post, Post))
        #self.assertEqual(str(post), 'test post')