from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostModelForm, CommentForm
from .models import Post, Comment

def create(request):
    # 만약, POST 요청이 오면
    if request.method == "POST":
        # 글을 작성하기
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
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
    comment_form = CommentForm()
    context = {
        'posts': posts,
        'comment_form': comment_form
    }
    return render(request, 'posts/list.html', context)
    
def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.user != request.user:
        return redirect('posts:list')
    post.delete()
    return redirect('posts:list')

def update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    if post.user != request.user:
        return redirect('posts:list')
    
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
    
def create_comments(request, post_id):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.post_id = post_id
        comment.save()
    return redirect('posts:list')

def like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    # 특정 유저가 특정 포스트를 좋아요 할 때
    # 만약 좋아요가 되어 있다면,
    if request.user in post.like_users.all():
        post.like_users.remove(request.user)
    # -> 좋아요를 해제하고,
    # 아니면
    else:
        post.like_users.add(request.user)
    # -> 좋아요를 한다.
    return redirect('posts:list')
