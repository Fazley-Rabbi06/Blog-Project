from django.urls import path
from App_Login import views

app_name="App_Login"
urlpatterns=[
    path('signup/',views.sign_up,name='signup'),
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout_page,name='logout'),
    path('profile/',views.profile_page,name='profile'),
    path('change_profile/',views.user_profile_change,name='change_profile'),
    path('password/',views.pass_change,name='pass_change'),
    path('add_profile_pic/',views.add_profile_pic,name='add_profile_pic'),
    path('change_profile_pic/',views.change_profile_pic,name='change_profile_pic')
    
]

 