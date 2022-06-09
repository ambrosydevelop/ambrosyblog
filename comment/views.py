from django.shortcuts import render,redirect
from .models import Comment
#coding: utf-8


def delete_comment(request,id,article_id):
    #Удаление комментария 
    comment = Comment.objects.get(id=id)
    if comment.author == request.user:
        comment.delete()
    return redirect('article',id=article_id)
