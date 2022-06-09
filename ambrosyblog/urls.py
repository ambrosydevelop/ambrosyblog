from django.contrib import admin
from django.urls import path
from article import views as a_views
from users import views as u_views
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static
from users.decorators import check_recaptcha
from django.views.generic.base import TemplateView
from comment import views as c_views


urlpatterns = [
    path('admin/', admin.site.urls),
    #Article app urls
    path('',a_views.index,name='index'),
    path('article/<int:id>/',a_views.article_detail,name='article'),
    path('articles/all/',a_views.all_article,name='all_article'),
    #Users app urls
    path('register/',check_recaptcha(u_views.register),name='register'),
    path('logout/',u_views.logout_view,name='logout'),
    path('login/',u_views.auth,name='login'),
    path('lc/',u_views.private_office,name='private_office'),
    #Comment urls
    path('delete/comment/<int:id>/<int:article_id>/',c_views.delete_comment,name='delete_comment'),
    #Other urls
    path('about-me/',TemplateView.as_view(template_name='article/about_me.html'),name='about_me'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)