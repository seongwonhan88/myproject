from django.conf import settings
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    photo = models.ImageField(upload_to='post')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pk']


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    content = models.TextField('comment')
    tags = models.ManyToManyField('HashTag',blank=True,)


class HashTag(models.Model):
    name = models.CharField(max_length=50,)

    def __str__(self):
        return self.name
