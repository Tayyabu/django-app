
from rest_framework.generics import ListAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from api.serializers import BlogPostSerializer
from core.models import BlogPost
from rest_framework import permissions
class ReadPost(ListAPIView):
    queryset=BlogPost.objects.all()
    serializer_class=BlogPostSerializer
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[JWTAuthentication]


