#_*_coding:utf-8_*_
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your models here.

class Article(models.Model):
    '''帖子表'''
    title = models.CharField(u'文章标题',max_length=255,unique=True)
    slug = models.SlugField("slug", max_length=50, unique=True, help_text="根据title生成的，用于生成页面url，必须唯一")
    category = models.ForeignKey("category",verbose_name=u'版块')
    head_img = models.ImageField(upload_to="uploads")
    content = models.TextField(u'文章内容')
    author = models.ForeignKey("UserProfile")
    publish_date = models.DateTimeField(auto_now=True)
    hidden = models.BooleanField(default=False)
    priority = models.IntegerField(u'优先级',default=1000)

    def __str__(self):
        return "<%s>" %(self.title)

    def get_absolute_url(self):
        return reverse('title', args=(self.slug,))

class Comment(models.Model):
    '''存储所有评论'''
    article = models.ForeignKey("Article")
    user = models.ForeignKey("UserProfile")
    comment = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now=True)
    '''层级评论(自关联)'''
    parent_comment = models.ForeignKey('self',related_name='p_comment',blank=True,null=True)
    def __str__(self):
        return "<%s,user:%s>" %(self.title,self.user)
class ThumbUp(models.Model):
    '''点赞'''
    article = models.ForeignKey("Article")
    user = models.ForeignKey("UserProfile")
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "<user:%s>" %(self.user)
class UserProfile(models.Model):
    '''账号信息表'''
    user = models.OneToOneField(User,)
    name = models.CharField(max_length=32)
    groups = models.ForeignKey("UserGroup")
    def __str__(self):
        return self.name
class Category(models.Model):
    '''帖子版块'''
    name = models.CharField(max_length=64,unique=True)
    admin = models.ForeignKey("UserProfile")
    def __str__(self):
        return self.name
class UserGroup(models.Model):
    '''用户组'''
    name = models.CharField(max_length=64,unique=True)
    def __str__(self):
        return self.name
