from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from App_Login.models import User,Userprofile
class Signup(UserCreationForm):
    email = forms.EmailField(label="Email Address",required=True)
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class UserProfileChange(UserChangeForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password')

class Profile_Pic(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = ('profile_pic',)
         