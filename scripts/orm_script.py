from core.models import BlogPost,PostReactions,CustomUser
def run():
   post = BlogPost.objects.first()
   print(post.reactions.all())

    
