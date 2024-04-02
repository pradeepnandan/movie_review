from .models import Genres
def menu_links(request):
    links=Genres.objects.all()
    return dict(links=links)
