from rest_framework.serializers import ModelSerializer
from core.models import BlogPost

class BlogPostSerializer(ModelSerializer):
    class Meta:
        model = BlogPost
        fields='__all__'
        
        
        
# class PostReactionSerializer(ModelSerializer):
#    class Meta:
#         model=PostReactions
#         fiels='__all__'
#         exclude=['post']
