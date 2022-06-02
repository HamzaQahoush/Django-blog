from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        'author': 'Hamza',
        'title': 'post 1',
        'content': " Hello from Home",
        "date": "August 27 2020"
    },
    {
        'author': 'Mohammad',
        'title': 'post 2',
        'content': " Hello from work",
        "date": "Sep 27 2022 "
    },
]


def home(request):
    context = {'posts': posts}

    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {'title': "about"})
