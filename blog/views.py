from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author':'Shedeed',
        'title':'Blog Post 1',
        'content': 'First post content',
        'date_posted':'January 13, 2020'
    },
    {
        'author':'Fadwa',
        'title':'Blog Post 2',
        'content': 'Second post content',
        'date_posted':'January 13, 2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
