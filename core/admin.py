from django.contrib import admin
from .models import CustomUser,BlogPost,PostReactions
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(BlogPost)
admin.site.register(PostReactions)
