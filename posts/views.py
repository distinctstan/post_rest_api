from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes

from .serializers import UpdateUserProfileSerializer, UserRegistrationSerializer,PostSerializer
from .models import Post

# Create your views here.

def home(request):
    return HttpResponse('''div>
                            <h1>Welcome to our posts rest api service.</h1> 
                            <p>
                                <strong>Visit these endpoints below to use our api:</strong> <br>
                                <span style="color:green">/all/post/</span> - To view all posts <br>
                                <span style="color:green">/create/post/</span> - To create a new post (Requires Authentication) <br>
                                <span style="color:green">/update/post/<post_id>/</span> - To update a post (Requires Authentication) <br>
                                <span style="color:green">/delete/post/<post_id>/</span> - To delete a post (Requires Authentication) <br>         
                                <span style="color:green">/update/user/profile/</span> - To update user profile (Requires Authentication) <br>         
                                <span style="color:green">/register/</span> - To register a new user <br>         
                                <span style="color:green">/token/</span> - To obtain a token for authentication <br>         
                                <span style="color:green">/token/refresh/</span> - To obtain a refresh token for authentication <br>         
                            </p>
                        </div>''')

@api_view(['POST'])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user_profile(request):
    user = request.user
    serializer = UpdateUserProfileSerializer(user,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
    user = request.user
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=user)
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def all_post(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts,many=True)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_post(request,pk):
    user = request.user
    post = Post.objects.get(id=pk)
    if post.author != user:
        return Response({'error':'You are not the author of this post'},status=status.HTTP_403_FORBIDDEN)
    serializer = PostSerializer(post,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_post(request,pk):
    post = Post.objects.get(id=pk)
    user = request.user
    if post.author != user:
        return Response({'error':'You are not the author of this post'},status=status.HTTP_403_FORBIDDEN)
    post.delete()
    return Response({'message':'Post deleted successfully'},status=status.HTTP_204_NO_CONTENT)
