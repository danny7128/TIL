"""testpjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("calculate/<int:number_1>/<int:number_2>", views.calculate),
    path("is-odd-even/<int:number_1>", views.is_odd_even),
    path("name_input", views.name_input),
    path("past_result", views.past_result),
    path("lorem_input", views.lorem_input),
    path("lorem_output", views.lorem_output),
]
