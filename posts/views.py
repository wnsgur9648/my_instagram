from django.shortcuts import render

def create(request):
    return render(request, 'posts/create.html')