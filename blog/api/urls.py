from django.urls import re_path
from . import views
from django.urls import path, include

urlpatterns = [
    # re_path(r'^posts/$', views.BlogPost.as_view(), name='posts'),
    # re_path(r'api/v1/', include('api.urls')),
    re_path(r'^posts/$', views.CreatePost.as_view(), name='posts'),
    path('users/', views.CreateUser.as_view(), name='create_user'),
]
