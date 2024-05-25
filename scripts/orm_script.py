from core.models import Comment
def run():
  for comment in Comment.objects.all():
    print(comment.author.email)
