from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


def index(request):
    posts = Post.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'posts': posts})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = PostForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


