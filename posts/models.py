from django.db import models
from django.conf import settings


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        verbose_name="author",
        related_name="posts",
        related_query_name="post",
        )
    title = models.CharField(verbose_name="title", max_length=50)
    body = models.TextField(verbose_name="body")
    created_at = models.DateTimeField(verbose_name="date post is created", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="date post is updated", auto_now=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'