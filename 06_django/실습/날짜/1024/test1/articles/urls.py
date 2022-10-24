from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('<int:article_pk>/', views.index, name='index'),
    path('<int:article_pk>/likes/', views.likes, name='likes'),
]
