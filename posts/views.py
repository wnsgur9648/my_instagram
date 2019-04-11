from django.shortcuts import render, redirect
from .forms import PostModelForm
from .models import Post

def create(request):
    # 만약, POST 요청이 오면
    if request.method == "POST":
        # 글을 작성하기
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:list')
    # 만약, GET 요청이 오면
    else:
    # post를 작성하는 form을 가져와 template에서 보여준다.
        form = PostModelForm()
        context = {
            'form': form
        }
        return render(request, 'posts/create.html', context)
def list(request):
    # 모든 Post를 보여줌
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts/list.html', context)
    
def delete(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('posts:list')

def update(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == "POST":
        form = PostModelForm(request.POST, instance = post)
        if form.is_valid():
            form.save()
            return redirect('posts:list')
    else:
        form = PostModelForm(instance=post)
        context = {
            'form': form
        }
        return render(request, 'posts/update.html', context)
    