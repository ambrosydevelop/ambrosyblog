from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    code = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='image')
    date = models.DateTimeField(datetime.now(),auto_now_add=True)

    def __str__(self):
        return self.title
class Like(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='article_field')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='author_field')
    like = models.BooleanField()

    def __str__(self):
        return self.author.username
class ArticleView(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='article_view_field')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_view_field')

    def __str__(self):
        return self.article.title