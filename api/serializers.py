from rest_framework.serializers import ModelSerializer
from core.models import BlogPost

class BlogPostSerializer(ModelSerializer):
    class Meta:
        model = BlogPost
        fields=['id','reactions']
        depth=1
        
