from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.text import slugify

from .models import Genres,Movies,Reviews
from registerapp.models import Users
from .frmMovies import AddMovieForm,EditMoviesForm,ReviewMoviesForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def index(request):
    cat=Genres.objects.all()
    # cat_dic={'cat_key': cat}
    movies = Movies.objects.all()
    paginator=Paginator(movies,8) #8 movies in one page
    page_num=request.GET.get('page') # get the page number from template while clicking the page number
    movies_by_page=paginator.get_page(page_num)
    # mov_dic={'movies_list': movies}

    movies_dic = {}
    sorted_movies_dic = {}
    try:
       # movies = Movies.objects.all()
        for movie in movies:
            review = Reviews.objects.filter(movie_id=movie.id)
            counter = 0
            rating = 0
            #print(type(review)) query set type
            for j in review:
                # rate=j.rating
                counter+=1
                rating += j.rating
            print(counter,rating,movie.movie_title)
            if counter==0:
                rating=0
            else:
                rating=round(rating/counter,1)

            movies_dic[movie.movie_title] = rating
        print(movies_dic)
        sorted_movies_dic = dict(sorted(movies_dic.items(), key=lambda item: item[1], reverse=True))
        print(sorted_movies_dic)
        #print(type(movies_dic)) type is dictionary
    except ObjectDoesNotExist:
        pass

    return render(request,'index.html', {'cat_key': cat,'movies_list_by_page': movies_by_page,'movie_dic':sorted_movies_dic})



# Add Movies
@login_required
def AddMovies(request):
    if request.method == 'POST':
        form_add = AddMovieForm(request.POST,request.FILES) # request.FILES is for images or files
        if form_add.is_valid():
            movie = form_add.save(commit=False)
            movie.added_by = request.user
            movie_title=form_add.cleaned_data['movie_title']
            movie.slug=slugify(movie_title)
            movie.save()
            return redirect('/')  # Redirected to login page
    else:
        form_add = AddMovieForm()
        # print(form)
    # return render(request, 'addMovies.html')
    return render(request, 'addMovies.html', {'form_add': form_add})
def EditMovies(request,pk):
    movie_to_edit = get_object_or_404(Movies, pk=pk)
    if request.method == 'POST':
        form_edit = EditMoviesForm(request.POST, instance=movie_to_edit)
        if request.user != movie_to_edit.added_by:  # Check if the current user is the one who added the movie
        # Handle unauthorized access
            messages.info(request, 'Not Authorised to Edit')
            #return redirect('/register/login', login_key)
            return redirect('/')

        if form_edit.is_valid():
            form_edit.save()
            return redirect('movies_app:EditMovies',pk)
    else:
        form_edit = EditMoviesForm(instance=movie_to_edit)
    return render(request,'editMovies.html',{'form_edit': form_edit})
   #    return render(request,'editMovies.html')
def DeleteMovies(request,pk):
    return render(request,'test.html')
@login_required
def ReviewMovies(request,pk):
    movie_list=[] #List of user details related to reviewd by
    movie_reviewed=Reviews.objects.all().filter(movie_id=pk)

    for review in movie_reviewed:
        #movie_reviewed_user=Users.objects.all().filter(id=review.user_id)
        movie_reviewed_user=Users.objects.get(id=review.user_id)
        movie_list.append(movie_reviewed_user)
    #print(movie_list)
    zip_data = zip(movie_reviewed, movie_list)
    movie = get_object_or_404(Movies, pk=pk)
    if request.method == 'POST':
        form_review = ReviewMoviesForm(request.POST)
        if form_review.is_valid():
            review_save=form_review.save(commit=False)
            review_save.user=request.user
            review_save.movie=movie
            review_save.save()
        #return render(request, 'movie_review.html')
        return redirect('movies_app:ReviewMovies',pk=pk)

            # return redirect('/')
            #movie_reviewed = Reviews.objects.all().filter(movie_id=pk)

        # return render(request, 'movie_review.html', {'movie': movie, 'movie_reviewed_l': movie_reviewed, 'zip_data': zip_data})
    #else:
        #user=request.user
        # user=user.username
        # form_review = ReviewMoviesForm() #To pre-populate username in the form

    return render(request, 'movie_review.html', {'movie': movie,'movie_reviewed_l':movie_reviewed,'zip_data':zip_data})


def Details(request,pk):
    movie_select=get_object_or_404(Movies,pk=pk)
    #print(movie_select)
    return render(request,'movieDetails.html',{'movie_select':movie_select})

def rate_count(request):
    counter=0
    movies_dic={}
    sorted_movies_dic={}
    try:
        movies=Movies.objects.all()
        for movie in movies:
            review = Reviews.objects.filter(movie_id=movie.id)
            print(review)
            for j in review:
                #rate=j.rating
                counter+=j.rating
            movies_dic[movie.movie_title]=counter
            sorted_movies_dic = dict(sorted(movies_dic.items(), key=lambda item: item[1],reverse=True))

        print(movies_dic)
    except ObjectDoesNotExist:
        pass
    return redirect('movies_app:index', {'movie_dic':sorted_movies_dic})
    #return render(request,'test.html', {'movie_dic':sorted_movies_dic})


def CatDetails(request,pk):
    movies=Movies.objects.filter(movie_genres=pk)
    return render(request,'movie_cat_det.html',{'movies':movies})
@login_required
def DeleteReview(request,pk,m_id):
    review=get_object_or_404(Reviews,pk=pk)
    if request.user != review.user:  # Check if the current user is the one who added the review
        # Handle unauthorized access
        messages.info(request, 'Not Authorised to Delete')
        # return redirect('/register/login', login_key)
        return redirect('/')
    else:
    # if review.is_valid():
        review.delete()
        # Get the previous URL from the request's 'HTTP_REFERER' header
        previous_url = request.META.get('HTTP_REFERER')
        # return render(request,'test.html')
        return redirect(previous_url)



