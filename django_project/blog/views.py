from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author' : 'CoreRim',
        'title' : 'title one',
        'content' : 'content one',
        'date_posted' : 'August 27, 2022',
    },
    {
        'author' : 'RimWorld',
        'title' : 'title two',
        'content' : 'content two',
        'date_posted' : 'August 28, 2022',
    },
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
# Create your views here.


