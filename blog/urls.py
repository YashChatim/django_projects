from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_blog_index, name='blog-index'),
    path('blogs', views.get_all_posts, name='all-posts'),
    path('blogs/<int:post_id>', views.get_post_detail, name='post-detail'),
]