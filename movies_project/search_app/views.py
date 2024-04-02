from django.shortcuts import render
from movies_app.models import Movies
from django.db.models import Q
# Create your views here.
def searchResult(request):
    movie=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        movie=Movies.objects.all().filter(Q(movie_title__icontains=query)|Q(hero_name__icontains=query))
        return render(request,'search.html',{'query':query,'movie':movie})