from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post, Category
# Create your tests here.

class Test_Create_Test(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')
        testuser1 = User.objects.create_user(username='test_user', password='123456789')
        test_post = Post.objects.create(category_id=1, title='Post Title', excerpt='Post Excerpt', content='Post Content', slug='post-title', author_id=1, status='published')

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        category = Category.objects.get(id=1)
        author = User.objects.get(id=1)
        excerpt = Post.excerpt
        content = Post.content
        status = Post.status
        self.assertEqual(f'{post.title}', 'Post Title')
        self.assertEqual(f'{post.author}', 'test_user')
        self.assertEqual(f'{post.category}', 'django')
        self.assertEqual(f'{post.slug}', 'post-title')
        self.assertEqual(f'{post.excerpt}', 'Post Excerpt')
        self.assertEqual(f'{post.content}', 'Post Content')
        self.assertEqual(f'{post.status}', 'published')
        self.assertEqual(str(post), 'Post Title')
        self.assertEqual(str(category), 'django')