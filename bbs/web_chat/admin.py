from django.contrib import admin
from .models import QQGroup
# Register your models here.
@admin.register(QQGroup)
class QQGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description','max_member_nums',)