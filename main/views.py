from django.shortcuts import render

# Create your views here.

def start(request):
    return render(request, 'main/start/index.html')

def all(request):
    return render(request, 'main/all/all.html')

def new(request):
    return render(request, 'main/new/new.html')

def news(request):
    return render(request, 'main/news/news.html')

def popular(request):
    return render(request, 'main/popular/pop.html')

def reg(request):
    return render(request, 'main/reg/reg.html')

def gamereview(request):
    return render(request, 'main/gamereview/grev.html')