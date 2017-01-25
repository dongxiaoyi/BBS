
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    url(r'dashboard/$', views.dashboard, name='web_chat'),

]+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

