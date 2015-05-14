from django.shortcuts import render
from .models import Post

# Create your views here.

def post_list(request):
    # return render(request, 'blog/post_list.html', {})
    posts=Post.objects.filter(published_date__isnull=False)
    return render(request,'blog/post_list2.html',{'posts': posts})
    pass
