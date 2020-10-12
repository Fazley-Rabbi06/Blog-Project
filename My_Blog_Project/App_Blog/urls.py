from django.urls import path
from App_Blog import views

app_name='App_Blog'

urlpatterns=[
    path('',views.Blog_list.as_view(),name='blog_list'),
    path('write/',views.Create_Blog.as_view(),name='create_blog'),
    path('blog_details/<int:id>',views.blog_details,name="blog_details"),
    path('liked/<pk>/',views.liked,name='liked_post'),
    path('unliked/<pk>/',views.unliked,name="unliked_post"),
    path('my_blogs',views.My_blog.as_view(),name="my_blogs"),
    path('update_blog/<pk>/',views.Update_blog.as_view(),name="update_blog"),
    path('delete_blog/<pk>/',views.Delete_blog.as_view(),name="delete_blog")

    
] 