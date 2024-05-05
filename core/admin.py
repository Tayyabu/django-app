from django.contrib import admin
from .models import CustomUser,BlogPost
admin.site.register(CustomUser)
admin.site.register(BlogPost)

