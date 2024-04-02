from django.contrib import admin
from .models import Reviews,Movies,Genres

# Register your models here.
admin.site.register(Movies)
admin.site.register(Genres)