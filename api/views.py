from django.shortcuts import render
from rest_framework import generics
from api.serializers import BlogPostSerializer

from core.models import BlogPost

class PostReadView(generics.RetrieveAPIView):
    queryset=BlogPost.objects.all()
    serializer_class=BlogPostSerializer

# Create your views here.
