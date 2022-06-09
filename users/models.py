from django.db import models
from django.contrib.auth.models import User


class Avatar(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_avatar',null=True,blank=True)
    avatar = models.ImageField(upload_to='avatar',default='avatar/image.png')

    def __str__(self):
        return self.user.username
