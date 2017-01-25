#_*_coding:utf-8_*_
from django import forms
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
import os,subprocess,time
import sys,os
sys.path.append('..')
from bbs import settings
class ArticleForm(forms.Form):
    title = forms.CharField(max_length=255,min_length=5)
    summary = forms.CharField(max_length=255,min_length=5)
    head_img = forms.ImageField()
    content = forms.CharField(min_length=10)
    category_id = forms.IntegerField()

def handle_upload(request,file):
    user_path = 'statics/imgs/upload/%s' % (request.user.userprofile.id)
    if not os.path.exists(user_path):
        os.mkdir(user_path)
    upload_file = "statics/imgs/upload/%s/%s" % (request.user.userprofile.id,file.name)
    with open(upload_file, 'wb+') as new_file:
        for chunk in file.chunks():
            new_file.write(chunk)
    #return 'statics/imgs/upload/%s/%s' %(request.user.userprofile.id,file.name)
    #return '/static/%s/%s' %(request.user.userprofile.id,file.name)


