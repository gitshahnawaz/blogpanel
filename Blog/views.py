from django.shortcuts import render, redirect
from app.models import Post

def BASE(request):
    return render(request,'Main/base.html')


def INDEX(request):
    popular_post = Post.objects.filter(section = 'Popular',status=1).order_by('-id')[0:3]
    recent_post = Post.objects.filter(section = 'Recent',status=1).order_by('-id')[0:3]
    main_post = Post.objects.filter(Main_post = True,status=1)[0:1]
    Editors_Pick = Post.objects.filter(section = 'Editors_Pick',status=1).order_by('-id')
    Trending = Post.objects.filter(section = 'Trending',status=1).order_by('-id')
    Inspiration = Post.objects.filter(section = 'Inspiration',status=1).order_by('-id')[0:5]
    Latest_Posts = Post.objects.filter(section = 'Latest_Posts',status=1).order_by('-id')[0:4]
    # print(post)
    context = {
        'popular_post':popular_post,
        'recent_post':recent_post,
        'main_post':main_post,
        'Editors_Pick':Editors_Pick,
        'Trending':Trending,
        'Inspiration':Inspiration,
        'Latest_Posts':Latest_Posts,
    }
    return render(request, 'Main/index.html',context)

def DETAIL(request, id):
    post = Post.objects.filter(id=id)[0]
    return render(request, 'Main/single.html',{'post':post})

