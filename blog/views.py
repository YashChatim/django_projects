from django.http import Http404
from django.shortcuts import render

all_posts = {
    1: {
        'title': 'Title 1',
        'description': 'Description 1'
    },
    2: {
        'title': 'Title 2',
        'description': 'Description 2'
    },
    3: {
        'title': 'Title 3',
        'description': 'Description 3'
    },
    4: {
        'title': 'Title 4',
        'description': 'Description 4'
    },
    5: {
        'title': 'Title 5',
        'description': 'Description 5'
    },
}

# Create your views here.
def get_blog_index(request):
    return render(request, 'blog/index.html', {
        'title': 'Blog Landing Page',
    })

def get_all_posts(request):
    return render(request, 'blog/all-posts.html', {
        'all_posts': all_posts,
        'title': 'All Posts',
    })

def get_post_detail(request, post_id):
    try:
        current_post = all_posts[post_id]
        return render(request, 'blog/post-detail.html', {
            'current_post': current_post,
        })
    except:
        raise Http404()