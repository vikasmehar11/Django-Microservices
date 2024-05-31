from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from rest_framework import status
import requests

class PostAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        return Response([self.formatPost(p) for p in posts])
    
    def formatPost(self, post):
        comments = requests.get(f'http://127.0.0.1:8000/api/posts/{post.id}/comments').json()
        return {
            'id': post.id,
            'title': post.title,
            'description': post.description,
            'comments': comments
        }
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
