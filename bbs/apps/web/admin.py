from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass
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
