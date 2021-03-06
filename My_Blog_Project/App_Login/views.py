from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from App_Login.forms import Signup,UserProfileChange,Profile_Pic
# Create your views here.

def sign_up(request): 
    form = Signup()
    registered = False
    if request.method == 'POST':
        form = Signup(data=request.POST)
        if form.is_valid(): 
            form.save()
            registered = True
    dict = {'form':form,'registered':registered}
    return render(request,'App_Login/signup.html',context=dict)


def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('App_Blog:blog_list'))
    return render(request,'App_Login/login.html',context={'form':form})
 
@login_required
def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Blog:blog_list'))

@login_required
def profile_page(request):
    return render(request,'App_Login/profile.html',context={})

 
@login_required
def user_profile_change(request):
    current_user = request.user
    form = UserProfileChange(instance=current_user)
    if request.method == 'POST':
        form = UserProfileChange(request.POST,instance=current_user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request,'App_Login/change_profile.html',context={'form':form})

@login_required
def pass_change(request):
    current_user = request.user
    changed = False
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user,request.POST)
        if form.is_valid():
            form.save()
            changed = True
    return render(request,'App_Login/pass_change.html',context={'form':form,'changed':changed})

    
@login_required
def add_profile_pic(request):
    form = Profile_Pic()
    if request.method == 'POST':
        form = Profile_Pic(request.POST,request.FILES)
        if form.is_valid():
            user_obj=form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request,'App_Login/add_profile_pic.html',context={'form':form})    

@login_required
def change_profile_pic(request):
    form = Profile_Pic(instance=request.user.userprofile)
    if request.method == 'POST':
        form = Profile_Pic(request.POST,request.FILES,instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request,'App_Login/add_profile_pic.html',context={'form':form})  