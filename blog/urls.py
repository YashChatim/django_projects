from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_blogs_index),
    path('blogs', views.get_all_blogs),
    path('blogs/<int:blog_id>', views.get_blog_id, name='current-blog'),
]