from django.shortcuts import render
from epp_api.models import Post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.

'''def home(request):
    return render(request,"post/index.html", {'posts':Post.objects.count(), 'dato': 22})'''

#Trayendo la Data desde la BD

'''def post_list(request):
    
    #posts=Post.objects.all() #Primera forma de traer data
    posts=Post._meta.model.objects.all() # Esta es otra forma de traer data

    #posts=Post.objects.filter(status='draft') # Realizando un filtro
    return render(request,'post/post_list.html',{'posts':posts})
'''

def post_list(request):
    
    object_list=Post.objects.filter(status="published")
    paginator = Paginator(object_list,3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,'post/post_list.html',{'posts':posts})
