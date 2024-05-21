from django.urls import path
from .views import CommentsAPIView, PostCommentAPIView

urlpatterns = [
    path('comments', CommentsAPIView.as_view(), name='comments'),
    path('posts/<str:pk>/comments', PostCommentAPIView.as_view(), name='post-comments')
]
