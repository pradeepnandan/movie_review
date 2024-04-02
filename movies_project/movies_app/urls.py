"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from . import views
from django.contrib import admin
from django.urls import path,include
app_name = 'movies_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('addmovies/',views.AddMovies,name='AddMovies'),
    path('details/<int:pk>/',views.Details,name='Details'),
    path('Cat_details/<int:pk>/',views.CatDetails,name='CatDetails'),
    path('editmovies/<int:pk>/',views.EditMovies,name='EditMovies'),
    path('deletemovies/<int:pk>/',views.DeleteMovies,name='DeleteMovies'),
    path('delete_review/<int:pk>/<int:m_id>/',views.DeleteReview,name='DeleteReview'),
    path('review/<int:pk>/',views.ReviewMovies,name='ReviewMovies'),
    path('count/',views.rate_count,name='rate_count')

]