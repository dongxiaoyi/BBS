from django.shortcuts import render,HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import sys
sys.path.append('..')
from web.models import Article
# Create your views here.
def index(request):
    articles = Article.objects.all()
    return render(request,"index.html",{'articles':articles})
def category(request,category_id):
    articles = Article.objects.filter(category_id=category_id)
    return render(request,"index.html",{'articles':articles})
def article_detail(request,article_id):
    try:
        article_obj = Article.objects.get(id=article_id)
    except ObjectDoesNotExist as e:
        return render(request,'404.html',{'err_msg':u'文章不存在'})
    return render(request,"article.html",{'article_obj':article_obj})