# blog/views.py
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# We use reverse_lazy as opposed to just reverse so that it won’t execute 
# the URL redirect until our view has finished deleting the blog post.
# whereas just the resverse will immediately redirect without waiting for 
# the delete action.

from .models import Post
# We are importing from the Django API the UpdateView class/object to later
# make our own Class out of it called BlogUpdateView

# Create your views here to populate data from database
# This is where the ORM of Django interacts with the database
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

# We are using Django's views.generic API by importing DetailView Class
# Then we are makeing this DetailView Class our own with BlogDetailView
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreatelView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__' # we only have two: title and author

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title','body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home') 
# It won't execute the URL redirect until our view has finished deleting 
# the blog post. In the Create/Update the model.py has the get_absolute_url() 
# function (with reverse-lazy to redirect to post_detail.html but when 
# we are deleting the post we cannot load the post_detail view 