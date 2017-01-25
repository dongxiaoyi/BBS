"""bbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
import sys
sys.path.append('..')
from web_chat import urls as chat_urls
sys.path.append('..')
from web import views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^chat/', include(chat_urls)),
    url(r'^$', views.index,name='index'),
    url(r'^category/(\d+)/$', views.category,name='category'),
    url(r'^article/(\d+)/$', views.article_detail, name='article_detail'),
    url(r'^article/new/', views.new_article, name='new_article'),
    url(r'^account/logout/', views.acc_logout, name='logout'),
    url(r'^account/login/', views.acc_login, name='login'),

]+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

