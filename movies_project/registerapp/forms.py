from django import forms
#from django.contrib.auth.models import Users
from .models import Users
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'email','password','phone_number']