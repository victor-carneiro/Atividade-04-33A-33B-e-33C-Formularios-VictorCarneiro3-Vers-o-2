"""django_project URL Configuration

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
from appDoVictor import views

urlpatterns = [
    path('',views.mPagina, name='mPagina'),
    path('movies', views.create_movie),
    path('fMovies', views.create_favourite_movie),
    path('movies/update/<id>', views.update_movie),
    path('fMovies/update/<id>', views.update_favourite_movie),
    path('movies/delete/<id>', views.delete_movie),
    path('fMovies/delete/<id>', views.delete_favourite_movie),
    path('admin/', admin.site.urls),
]

