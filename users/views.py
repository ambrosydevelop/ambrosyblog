from django.shortcuts import redirect, render
from article.models import Article,Like
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from .models import Avatar
from .forms import UserRegistrationForm,UserLoginForm
from django.http import JsonResponse
from django.contrib.auth.models import User
#coding: utf-8


def register(request):
    #Прм переходе по url 'register' вызывается данная функция,служит для регестрации
    if request.user.is_anonymous:
        form = UserRegistrationForm()
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if request.recaptcha_is_valid:
                if form.is_valid():
                    user = form.save()
                    login(request,user)
                    Avatar.objects.create(user=request.user)
                    return redirect('index')
    else:
        return redirect('index')
    return render(request,'users/register.html',{'form':form})
@login_required
def logout_view(request):
    #Аутентификация
    logout(request)
    return redirect('index')
@login_required
def private_office(request):
    #Показывает профиль пользователя,если тот авторизован
    if request.POST.get('action') == 'post':
        username = request.POST.get('username')

        response_data = {}
        response_data['username'] = username.replace(' ','')

        try:
            User.objects.get(username=username.replace(' ',''))
        except User.DoesNotExist:
            user = User.objects.get(username=request.user.username)
            user.username = username.replace(' ','')
            user.save()    
            return JsonResponse(response_data)
        
    avatar = Avatar.objects.get(user=request.user)

    context = {
        'avatar':avatar,
        'articles':[Article.objects.get(id=x.id) for x in Like.objects.filter(like=True,author=request.user)][:4],
    }
    return render(request,'users/private_office.html',context)
def auth(request):
    #Авторизация
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(
            request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
        )
        login(request,user)
        return redirect('index')
    return render(request,'users/login.html',{'form':form})