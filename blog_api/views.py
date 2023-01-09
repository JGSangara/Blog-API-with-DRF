from django.shortcuts import render
from rest_framework import generics, permissions, status, views
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Post
from users.models import User

from .serializers import CustomUserSerializer, LoginSerializer, PostSerializer
from django.contrib.auth import authenticate, login
# Create your views here.


class PostPermission(permissions.BasePermission):
    message = "You are not authorized to perform this action."

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user


class PostList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostPermission):
    permission_classes = [PostPermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CustomUserCreate(generics.CreateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return CustomUser.objects.all()


class LoginView(views.APIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)

        if user:
            login(request, user)
            return Response(self.serializer_class(user).data)
        else:
            return Response(
                {"error": "Wrong Credentials"},
                status=status.HTTP_400_BAD_REQUEST,
            )
