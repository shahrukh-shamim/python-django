from django.shortcuts import render
from rest_framework import generics, status
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog
from django.urls import reverse_lazy
from .serializers import BlogSerializer
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
class BlogPageView(TemplateView):
    template_name = 'blogs/blogs.html'

    def get_context_data(self, **kwargs):
        configs = Blog.objects.filter()
        context = super().get_context_data(**kwargs)

        for config in configs:
            context[config.key] = config.value
        return context

class BlogListView(ListView):
    model = Blog
    template_name = 'blogs/list.html'
    context_object_name = 'blogs'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blogs/detail.html'
    context_object_name = 'blog'

class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'content']
    template_name = 'blogs/form.html'
    success_url = reverse_lazy('blog_list')

    @method_decorator(login_required(login_url=reverse_lazy('login')))
    def dispatch(self, request, *args, **kwargs):
        # Your view logic here (optional for further processing after authentication check)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_type'] = 'create'
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content']
    template_name = 'blogs/form.html'
    success_url = reverse_lazy('blog_list')
    pk_url_kwarg = 'pk'

    @method_decorator(login_required(login_url=reverse_lazy('login')))
    def dispatch(self, request, *args, **kwargs):
        # Your view logic here (optional for further processing after authentication check)
        return super().dispatch(request, *args, **kwargs)

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blogs/confirm_delete.html'
    success_url = reverse_lazy('blog_list')
    pk_url_kwarg = 'pk'

    @method_decorator(login_required(login_url=reverse_lazy('login')))
    def dispatch(self, request, *args, **kwargs):
        # Your view logic here (optional for further processing after authentication check)
        return super().dispatch(request, *args, **kwargs)