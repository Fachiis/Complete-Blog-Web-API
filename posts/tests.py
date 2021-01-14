from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post


class BlogTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser = User.objects.create_user(
            username='testuser', password='test1234'
        )
        testuser.save()

        post_test = Post.objects.create(
            author=testuser, title='Test', body="Yeah..."
        )
        post_test.save()

    def test_blog_content(self):
        post = Post.objects.get(pk=1)
        author = f'{post.author}'
        title = f'{post.title}' #Python f'{}' is used to pass the value of the key used
        body = f'{post.body}'
        self.assertEqual(author, 'testuser')
        self.assertEqual(title, 'Test')
        self.assertEqual(body, 'Yeah...')