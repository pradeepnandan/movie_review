from django.db import models
from registerapp.models import Users

# Create your models here.
class Genres(models.Model):
    # Define choices for the dropdown menu
    CHOICES = [
        ('ActionMovies', 'Action Movies'),
        ('FamilyEntertainment','Family Entertainment'),
        ('HorrorMovies', 'Horror Movies'),
        ('ThrillerMovies', 'Thriller Movies'),
        ('ScienceFiction (Sci-Fi) Movies', 'Science Fiction (Sci-Fi) Movies'),
        ('RomanceMovies', 'Romance Movies'),
        ('FantasyMovies', 'Fantasy Movies'),
        ('AnimationMovies:', 'Animation Movies:'),
    ]

    # Add a CharField with choices
    movie_type = models.CharField(max_length=250, choices=CHOICES,unique=True)
    cat_img=models.ImageField(upload_to='img',blank=True)
    def __str__(self):
        return self.movie_type

class Movies(models.Model):
    LANGUAGES = [
        ('Malayalam', 'Malayalam'),
        ('Tamil', 'Tamil'),
        ('Hindi', 'Hindi'),
        ('English', 'English'),
        ('Kannada','Kannada'),
    ]
    movie_title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=50, unique=True)
    movie_genres=models.ForeignKey(Genres,on_delete=models.CASCADE)
    language=models.CharField(max_length=250,choices=LANGUAGES,unique=False)
    director_name = models.CharField(max_length=250)

    # category=models.CharField(max_length=250,blank=True)
    poster=models.ImageField(upload_to='movies',blank=True)
    hero_name = models.CharField(max_length=250)
    heroin_name = models.CharField(max_length=250)
    movie_description = models.TextField(blank=True)
    released=models.DateField()
    added_by=models.ForeignKey(Users,on_delete=models.CASCADE)
    link_trailer=models.URLField(blank=True)
    trending=models.BooleanField(default=True)
    active=models.BooleanField(default=True)
    banner_img=models.ImageField(upload_to='movies',blank=True)

    def __str__(self):
        return self.movie_title

class Reviews(models.Model):
    movie=models.ForeignKey(Movies,on_delete=models.CASCADE)
    user=models.ForeignKey(Users,on_delete=models.CASCADE)
    review=models.TextField()
    date_review=models.DateTimeField(auto_now=True)
    rating=models.IntegerField()