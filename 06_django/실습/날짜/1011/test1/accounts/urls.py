from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/', views.list, name='list'),
    path('accounts/<int:pk>/', views.detail, name='detail'),
]
