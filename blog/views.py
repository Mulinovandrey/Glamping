# from django.http import HttpResponse
# from django.shortcuts import render
# from django.views.generic import TemplateView

from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Post, Category, Tag
from django.db.models import F



class BlogView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Glamping : Blog'
        return context


class GetPost(DetailView):
    model = Post
    template_name = 'blog/blog-single.html'
    # slug_url_kwarg = "slug"
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context
