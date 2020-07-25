from django.shortcuts import render

posts = [
    {
        'author': 'Salty91',
        'title': 'First scratch',
        'content': 'First post content',
        'date_posted': 'July 22, 2020'
    },
    {
        'author': 'Ashley Maddison',
        'title': 'Scratch number 2',
        'content': 'Second post content',
        'date_posted': 'July 23, 2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
