from django.contrib import messages, auth
from django.http import HttpResponseRedirect
# from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Users
from movies_app.models import Genres,Movies
from .forms import UserProfileForm

# Create your views here.
def register(request):
    return render(request,'register.html')

def register_submit(request):

   if request.method=='POST':
       username=request.POST['username']
       firstname = request.POST['first_name']
       lastname = request.POST['last_name']
       password = request.POST['password']
       cpassword = request.POST['re_password']
       email = request.POST['email']
       if password==cpassword:
           if Users.objects.filter(username=username).exists():
               messages.info(request,'Already Username taken')
               return redirect('register')
           elif Users.objects.filter(email=email).exists():
               messages.info(request,'Already email taken')
           else:
               user=Users.objects.create_user(username=username,first_name=firstname,last_name=lastname,password=password,email=email)
               user.save()
               messages.info(request,'User is Added')
               return redirect('/')
       else:
           messages.info(request,'Passwords not matching')
           return redirect('register')
       return redirect('/')
   return render(request,'register.html')

def login(request):
    cat = Genres.objects.all()
    movies = Movies.objects.all()
    if request.method=='POST':
        login_key=False
        username=request.POST['username']
        password=request.POST['password']
        authuser=auth.authenticate(username=username,password=password)
        if authuser is not None:
            login_key=True
            auth.login(request,authuser)
            return redirect('/')

            # return render (request,'index.html',{'login_key':login_key,'cat':cat,'movies_list': movies})
        else:
            messages.info(request,'Not Authorised User')
            return redirect('/register/login',login_key)
    return render(request, 'login.html')
    #return HttpResponseRedirect('/register/login/')
def login_submit(request):
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


# def edit_profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Profile updated successfully.')
#             return redirect('edit_profile')
#     else:
#         form = UserProfileForm(instance=request.user)  # Pre-fill form with user data
#     return render(request, 'edit_profile.html', {'form': form})



def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            # saving without commit and assigning to user
            user = form.save(commit=False)
            # Check if password field is filled
            if form.cleaned_data.get('password'):
                # Set the password with hash using set_password() method
                user.set_password(form.cleaned_data['password'])
            #     saving
            user.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('edit_profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})
