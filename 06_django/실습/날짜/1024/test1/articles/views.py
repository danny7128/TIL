from django.shortcuts import render,redirect
from . models import Article

# Create your views here.
def index(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article':article
    }
    return render(request, 'articles/index.html',context)

def likes(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    # if request.user in article.like_users.all():
    if article.like_users.filter(id=request.user.id).exists():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    
    return redirect('articles:index',article_pk)

