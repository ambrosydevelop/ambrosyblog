from django.db import models
from article.models import Article
from django.contrib.auth.models import User
from datetime import datetime


class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='article')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    content = models.TextField(max_length=350)
    date = models.DateTimeField(datetime.now(),auto_now_add=True)

    def __str__(self):
        return self.author.username