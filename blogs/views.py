from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404

from .models import BlogSpot
from .forms import BlogFrom

def home(request):
    blogs = BlogSpot.objects.order_by('-date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/home.html',context)

@login_required
def new_post(request):
    if request.method != 'POST':
        form = BlogFrom()
    else:
        form = BlogFrom(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:home')
    context = {'form':form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
    post = BlogSpot.objects.get(id=post_id)
    if post.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = BlogFrom(instance=post)
    else:
        form = BlogFrom(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:home')
    context = {'form':form, 'post_id':post_id}
    return render(request, 'blogs/edit_post.html',context)
