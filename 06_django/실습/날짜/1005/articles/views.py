from django.shortcuts import render, redirect
from .models import Review

# Create your views here.
def index(request):
    k = Review.objects.all()
    context = {
        "v": k,
    }
    return render(request, "articles/index.html", context)


def create(request):
    if request.method == "GET":
        k = request.GET
        context = {"k": k}
        return render(request, "articles/create.html", context)
    else:
        title = request.POST.get("title")
        content = request.POST.get("content")
        Review.objects.create(title=title, content=content)

        return redirect("articles:index")


def detail(request, pk):
    k = Review.objects.get(pk=pk)
    context = {
        "v": k,
    }
    return render(request, "articles/detail.html", context)


def delete(request, pk):
    Review.objects.get(pk=pk).delete()
    return redirect("articles:index")


def update(request, pk):
    k = Review.objects.get(pk=pk)
    if request.method == "POST":
        k_t = request.POST.get("title")
        k_c = request.POST.get("content")

        k.title = k_t
        k.content = k_c
        k.save()
        return redirect("articles:index")
    else:
        context = {
            "c": k,
        }

    return render(request, "articles/update.html", context)
