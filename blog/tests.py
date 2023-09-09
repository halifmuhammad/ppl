from django.test import TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.
class ModelTesting(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title='test post', author='test', message='test message')
    
    def test_post_model(self):
        post = self.post
        self.assertTrue(isinstance(post, Post))
        self.assertEqual(str(post), 'test post')
    
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        post_titles = [post.title for post in response.context['posts']]
        self.assertListEqual(post_titles, ['test post'])

    def test_add_post_view_valid_data(self):
        data = {
            'title':'test post', 'author':'test', 'message':'test message'
        }
        response = self.client.post(reverse('add_post'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 2)

    def test_add_post_view_invalid_data(self):
        data = {
            'name':'test post'
        }
        response = self.client.post(reverse('add_post'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)
        self.assertTrue(response.context['failed'])






