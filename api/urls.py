from django.urls import path
from . import views

urlpatterns = [
  path('reactions/<int:pk>',views.PostReadView.as_view(),name="reactions")
]