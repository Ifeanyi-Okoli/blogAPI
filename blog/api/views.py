from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer, UserSerializer
from .models import Post
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
# Create your views here.

# @api_view(['GET', 'POST'])
# def posts(request):
#     if request.method == 'GET':
#         post = Post.objects.all()
#         serializer = PostSerializer(post, many=True)
#         data = serializer.data
#         return Response(data, status=status.HTTP_200_OK) 
#     elif request.method == 'POST':
#         data = JSONParser.parse(request)
#         serializer = PostSerializer(data, raise_exception=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        



class BlogPost(APIView):
    def get(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
         
        return Response({'message': 'post created successfully'}, status=status.HTTP_201_CREATED)
        return Response( serializer.data, status=status.HTTP_201_CREATED)
        

class CreateUser(APIView):
    # serializer_class =PostSerializer
    # authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'message': 'user created successfully'})   
    
class CreatePost(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class =PostSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]