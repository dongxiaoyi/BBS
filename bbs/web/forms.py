#_*_coding:utf-8_*_
from django import forms
import os,subprocess
class ArticleForm(forms.Form):
    title = forms.CharField(max_length=255,min_length=5)
    summary = forms.CharField(max_length=255,min_length=5)
    head_img = forms.ImageField()
    content = forms.CharField(min_length=10)
    category_id = forms.IntegerField()

def handle_upload_file(request,f):
    print(f.name)
    base_img_upload_path = './statics/imgs/upload/'
    user_path = "%s%s" % (base_img_upload_path,str(request.user.userprofile.id))
    print(user_path)
    if not os.path.isdir(user_path):
        create_menu(user_path)
    with open('%s/%s' % (user_path,f.name),'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
        destination.close()
    return "/tatics/imgs/upload/%s/%s" % (request.user.userprofile.id,f.name)
def create_menu(path):
    os.mkdir(path)

