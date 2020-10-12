from django.shortcuts import render
from django.views.generic import View,CreateView,UpdateView,DeleteView,DetailView,ListView,TemplateView
from App_Blog.models import Blog,Comment,Like,User
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
from App_Blog.forms import CommentForm

class My_blog(LoginRequiredMixin,TemplateView):
    template_name = 'App_Blog/my_blog.html'

class Create_Blog(LoginRequiredMixin,CreateView):
    model = Blog
    template_name = 'App_Blog/create_blog.html' 
    fields = ('blog_title','blog_content','blog_image') 
    def form_valid(self,form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(" ","/")+"/"+str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('index'))

class Blog_list(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'App_Blog/blog_list.html'
 
    

@login_required
def blog_details(request,id):
    blog = Blog.objects.get(pk=id)
    comment_form = CommentForm()
    already_liked = Like.objects.filter(blog=blog,user=request.user)
    if already_liked:
        liked = True
    else:
        liked = False
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_obj = comment_form.save(commit=False)
            comment_obj.user = request.user
            comment_obj.blog = blog
            comment_obj.save()
            return HttpResponseRedirect(reverse('App_Blog:blog_details',args={id}))
    return render(request,'App_Blog/blog_details.html',context={'blog':blog,'comment_form':comment_form,'liked':liked}) 

@login_required
def liked(request,pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user 
    already_liked = Like.objects.filter(blog=blog,user=user)
    if not already_liked:
        liked = Like(blog=blog,user=user)
        liked.save()
    return HttpResponseRedirect(reverse('App_Blog:blog_details',args={pk}))

@login_required
def unliked(request,pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user 
    already_liked = Like.objects.filter(blog=blog,user=user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('App_Blog:blog_details',args={pk}))


class Update_blog(LoginRequiredMixin,UpdateView):
    model = Blog
    fields = ('blog_title','blog_content','blog_image')
    template_name = 'App_Blog/edit_blog.html'
    def get_success_url(self,**args):
        return reverse_lazy('App_Blog:blog_details',args={self.object.pk})

# @login_required
# def delete_blog(request,pk):
#     blog = Blog.objects.get(pk=pk)
#     blog.delete()
#     return HttpResponseRedirect(reverse('App_Blog:blog_list'))

class Delete_blog(LoginRequiredMixin,DeleteView):
    model = Blog
    template_name = 'App_Blog/delete_blog.html'
    success_url = reverse_lazy('App_Blog:blog_list')
