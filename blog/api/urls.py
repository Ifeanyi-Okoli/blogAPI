from django.urls import re_path
from . import views
from django.urls import path, include

urlpatterns = [
    re_path(r'posts/$', views.posts, name='posts'),
    # re_path(r'api/v1/', include('api.urls')),
]
