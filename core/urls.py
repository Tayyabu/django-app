from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("post/", views.create_post, name="create_post"),
    path("post/edit/<int:pk>", views.edit_post, name="edit_post"),
    path("post/delete/<int:pk>", views.delete_post, name="delete_post"),
    path("post/<int:pk>", views.post_page, name="post"),
    path("comment/delete/<int:pk>", views.remove_comment, name="remove_comment"),
]
