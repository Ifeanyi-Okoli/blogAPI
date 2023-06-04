from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer
from .models import Post
# Create your views here.

@api_view(['GET'])
def posts(request):
    post = Post.objects.all()
    serializer = PostSerializer(post, many=True)
    data = serializer.data
    return Response(data, status=status.HTTP_200_OK) 