from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

def signup(request):
    # 회원가입
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('posts:list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
        return redirect('posts:list')
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form':form})

def logout(request):
    auth_logout(request)
    return redirect('posts:list')

def profile(request, username):
    # username을 가진 유저의 상세 정보를 보여주는 페이지
    profile = get_object_or_404(get_user_model(), username=username)
    return render(request, 'accounts/profile.html', {'profile': profile})

def delete(request):
    # 계정을 삭제한다. == DB에서 user를 삭제한다.
    if request.method == 'POST':
        request.user.delete()
        return redirect('posts:list')
    return render(request, 'accounts/delete.html')

@login_required
def follow(request, user_id):
    person = get_object_or_404(get_user_model(), pk=user_id)
    # 만약 이미 팔로우한 사람이라면
    if request.user in person.followers.all():
        person.followers.remove(request.user)
    # -> 언팔
    # 아니면,
    else:
        person.followers.add(request.user)
    # -> 팔로우
    return redirect('profile', person.username)