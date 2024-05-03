from django.contrib import admin
from .models import CustomUser,BlogPost
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(BlogPost)
