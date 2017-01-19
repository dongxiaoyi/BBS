from django.contrib import admin
from .models import *
from .forms import *
from django.core.urlresolvers import reverse

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'head_img', 'content', 'publish_date', 'hidden', 'priority',)
    list_display_links = ('title', 'category', 'author')
    list_per_page = 50
    ordering = ['publish_date']
    search_fields = ['title', 'category', 'author', 'content']
    exclude = ['publish_date', ]
    prepopulated_fields = {'slug': ('title',), }


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(UserGroup)
class UserGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(ThumbUp)
class ThumbUpAdmin(admin.ModelAdmin):
    pass
