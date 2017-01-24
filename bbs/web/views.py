#_*_coding:utf-8_*_
from .models import Article
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate,login,logout
from .forms import ArticleForm,handle_upload
import sys,os
sys.path.append('..')
from web.models import Article,Category
from bbs import settings
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
def acc_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
def acc_login(request):
    err_msg = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            #登录动作，生成session
            login(request,user)
            return HttpResponseRedirect('/')
        else:
            err_msg = "Wrong username or password"
    return render(request,'login.html',{'err_msg':err_msg})
def new_article(request):
    form = ArticleForm(request.POST,request.FILES)
    if form.is_valid():
        print("--form data",form.cleaned_data)
        form_data = form.cleaned_data
        form_data['author_id'] = request.user.userprofile.id
        old_img_name = str(form_data['head_img'])

        handle_upload(request,request.FILES['head_img'])
        form_data['head_img'] = "%s/%s"%(request.user.userprofile.id,old_img_name)
        new_article_obj = Article(**form_data)
        new_article_obj.save()
        return render(request,'new_article.html',{'new_article_obj':new_article_obj})
    else:
        print('err',form.errors)
    category_list = Category.objects.all()
    return render(request,'new_article.html',{'category_list':category_list})