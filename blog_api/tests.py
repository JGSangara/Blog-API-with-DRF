from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post, Category
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient

# Create your tests here.

class PostTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username = 'test_user 1', password='123456789')
        self.category = Category.objects.create(name='django')
        self.post = Post.objects.create(category_id=1, title='Post Title', excerpt='Post Excerpt', content='Post Content', slug='post-title', author_id=1, status='published')
        self.valid_payload = { 'category_id': 1, 'title': 'Post Title', 'excerpt': 'Post Excerpt', 'content': 'Post Content', 'slug': 'post-title', 'author_id': 1, 'status': 'published' }

    def test_create_valid_post(self):
        url = reverse('blog_api:listcreate')
        response = self.client.post(url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all_posts(self):
        url = reverse('blog_api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_post(self):
        url = reverse('blog_api:detailcreate', kwargs={'pk': self.post.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
