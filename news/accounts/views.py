from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm


def index(request):
    news = News.objects.all()
    return render(request,'accounts/index.html', {'title': 'Главная страница сайта', 'news': news})


def about(request):
    return render(request,'accounts/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма быда не верной'

    form = NewsForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request,'accounts/create.html', context)