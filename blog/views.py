from django.shortcuts import render

posts = [
    {
        'author': 'Dania',
        'title': 'Blog Post 1',
        'content': 'first post content',
        'date_posted': 'August 26, 2024'
    },
    {
        'author': 'Mohammedelhassan',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 26, 2025'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request,'blog/home.html',context)



def about(request):
    return render(request,'blog/about.html',{'title': 'About'})