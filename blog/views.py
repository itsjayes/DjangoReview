from django.shortcuts import render

def list_post(request):
    return render(request, 'blog/posts.html', {})