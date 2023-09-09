from django.shortcuts import render

from .models import Post
from .forms import PostForm
from django.http import HttpResponseRedirect



# Create your views here.
def index(request):
    posts = Post.objects.all()
    response = {'posts': posts}
    return render(request, 'index.html', response)

def add_post(request):
    failed = False
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/blog')
        else:
            failed = True
    
    form = PostForm()
    return render(request, 'add.html', {'form':form, 'failed':failed})
