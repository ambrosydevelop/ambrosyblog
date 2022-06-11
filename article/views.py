from .models import Article
from django.shortcuts import render
from comment.models import Comment
from django.http import JsonResponse
from .models import Like
from django.core.exceptions import ObjectDoesNotExist
from .models import ArticleView
#coding: utf-8


def index(request):
    #Главная страница
    context = {
        'articles':Article.objects.all()[:6],
    }
    return render(request,'article/index.html',context)
def all_article(request):
    #Все записи
    context = {
        'articles':Article.objects.all(),
        'is_show_all':True,
    }
    return render(request,'article/index.html',context)
def article_detail(request,id):
    #При переходе по ссылке к статье, получает данные из url и выводит в html шаблоне
    article = Article.objects.get(id=id)
    try: #Если пользователь просмотрел эту запись
        ArticleView.objects.get(article=article,author=request.user)
    except ArticleView.DoesNotExist: #Если пользователь НЕ просмотрел эту запись
        ArticleView.objects.create(article=article,author=request.user)

    if not request.user.is_anonymous:
        if request.POST.get('action') == 'post':
            content = request.POST.get('content')

            response_data = {}
            response_data['content'] = content

            if content:
                comment = Comment.objects.create(
                    article=article,
                    author=request.user,
                    content=content,
                    )
                response_data['number'] = Comment.objects.filter(article=article).count()
                response_data['id'] = comment.id
                
                return JsonResponse(response_data)
            else:
                try: #Если такой объект существует
                    like = Like.objects.get(article=article,author=request.user) 
                    if like.like:
                        like.like = False
                    else:
                        like.like = True
                    like.save() #Сохраняем параметры 
                except ObjectDoesNotExist: #Если такого объекта не существует
                    like = Like.objects.create(
                        article=article,
                        author=request.user,
                        like=True,
                    )
                response_data_like = {}
                response_data_like['number'] = Like.objects.filter(article=article,like=True).count()

                return JsonResponse(response_data_like)
    context = {
        'article':Article.objects.get(id=id),
        'comments':Comment.objects.filter(article=article),
        'like':Like.objects.filter(article=article,like=True),
        'number_of_views':ArticleView.objects.filter(article=article),
    }
    return render(request,'article/article.html',context)

