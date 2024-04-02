from django import forms
from .models import Movies, Reviews

class AddMovieForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Movies
        fields = ['movie_title', 'movie_genres', 'language','director_name','poster','hero_name','heroin_name','movie_description','released','link_trailer','banner_img']
        widgets = {
            'released': forms.DateInput(attrs={'type': 'date'}),

        }
class EditMoviesForm(forms.ModelForm):
    class Meta:
        model=Movies
        fields= ['movie_title', 'movie_genres', 'language','director_name','poster','hero_name','heroin_name','movie_description','released','link_trailer']
        widgets = {
            'released': forms.DateInput(attrs={'type': 'date'}),

      }

class ReviewMoviesForm(forms.ModelForm):
    class Meta:
        model=Reviews
        fields=['review','rating']
        # widgets = {
        #     'date_review': forms.DateInput(attrs={'type': 'date'}),
        # }