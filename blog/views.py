from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import BlogPost
from django.urls import reverse_lazy

class BlogListView(ListView):
    model = BlogPost
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = BlogPost
    template_name = 'add_new.html'
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = BlogPost
    template_name = 'post_edit.html'
    fields = '__all__'
    # fields = [ 'title', 'body']

class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
