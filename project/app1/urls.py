from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView



urlpatterns = [
    path('',views.home,name="home"),
    path('register/',views.register,name="register"),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('post/', views.post, name='post'),
    path('search/',views.search,name="search"),
    path('create_post/', views.create_post, name='create_post'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
    path('comment_post/<int:post_id>/', views.comment_post, name='comment_post'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]



