from django.shortcuts import render
from .models import Post
def main(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, 'index.html', context)
