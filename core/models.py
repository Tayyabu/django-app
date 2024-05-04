


from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.db.models.signals import post_save
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    
    # Add your custom fields here
    # For example:
    # bio = models.TextField(blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email



# Create your models here.
class BlogPost(models.Model):
    title=models.CharField(max_length=70)
    content=models.TextField()
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE,default=None)
    created_at=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='uploads/posts/',default="media/uploads/posts/4.png")
    # video=models.FieldFile(upload_to='uploads/posts/videos')
    def __str__(self):
        return self.title
    

class PostReactions(models.Model):
    coffee=models.PositiveBigIntegerField(default=0)
    rocket=models.PositiveBigIntegerField(default=0)
    thumbsUp=models.PositiveBigIntegerField(default=0)
    heart=models.PositiveBigIntegerField(default=0)
    wow=models.PositiveBigIntegerField(default=0)
    post=models.ForeignKey(BlogPost,on_delete=models.CASCADE,related_name='reactions')
    class Meta:
        verbose_name_plural='Postreactions'



def react_to_post(created,instance,*args, **kwargs):
    if created:
        PostReactions.objects.create(post=instance)



post_save.connect(react_to_post,sender=BlogPost)

