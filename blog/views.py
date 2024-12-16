from django.http import Http404
from django.shortcuts import render

all_blogs = {
    1: 'Blog 1',
    2: 'Blog 2',
    3: 'Blog 3',
    4: 'Blog 4',
    5: 'Blog 5',
}

# Create your views here.
def get_blogs_index(request):
    return render(request, 'blog/index.html', {
        'title': 'Blogs Landing Page',
    })

def get_all_blogs(request):
    return render(request, 'blog/blogs.html', {
        'all_blogs': all_blogs,
        'title': 'All Blogs',
    })

def get_blog_id(request, blog_id):
    try:
        current_blog = all_blogs[blog_id]
        return render(request, 'blog/blog.html', {
            'current_blog': current_blog,
            'title': f'Blog {current_blog}'
        })
    except:
        raise Http404()