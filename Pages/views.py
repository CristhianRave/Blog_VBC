from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import FormView
from django.views.generic import (
    ListView, 
    CreateView, 
    TemplateView,
    DetailView, 
    DeleteView,
    UpdateView
)

#Imports Locals
from .models import Page, Category
from Pages.forms import ArticleForm


# -----------------------------------------------------------


class ArticleIndividual (LoginRequiredMixin, DetailView):
    template_name = 'posts/entrada_individual.html'
    model = Page
    context_object_name = 'blog'
     
    login_url = 'Login'


# -----------------------------------------------------------


class Blog (LoginRequiredMixin, ListView):
    template_name = 'posts/entradas_blog.html'
    model = Page
    paginate_by = 6
    context_object_name = 'articles'
     
    login_url = 'Login'


# -----------------------------------------------------------


class Category_new (LoginRequiredMixin, ListView):
    template_name = 'posts/category.html'
    model = Page
     
    login_url = 'Login'


    def get_context_data(self):

        category_id = self.kwargs['category_id']
        articles = Page.objects.filter(categories=category_id)
        cat = Category.objects.get(id=category_id)

        paginator = Paginator(articles, 6)  # cantidad de articulos por pagina
        page = self.request.GET.get('page')  # Recogemos el parametro 'page'
        page_articles = paginator.get_page(page)  # Pasamos el numero de la pagina

        return {
            'cat' : cat,
            'articles': page_articles,
            'page_obj': page_articles,
        }
    

# -----------------------------------------------------------


class CreateArticle (LoginRequiredMixin, CreateView):
    model = Page
    template_name = 'posts/create_article.html'
    form_class = ArticleForm
    success_url = '/blog'
     
    login_url = 'Login'


    def form_valid(self, form):
        article_new = form.save(commit=False)
        user_id = self.request.POST.get('user')
        article_new.user_id = user_id
        article_new.slug = f"{user_id}-{article_new.title}"
        article_new.save()

        return super(CreateArticle, self).form_valid(form)


# -----------------------------------------------------------


class EditarArticle (LoginRequiredMixin, DetailView):
    template_name = 'posts/editar.html'
    model = Page
    context_object_name = 'article'
     
    login_url = 'Login'


# -----------------------------------------------------------


class UpdateArticle (LoginRequiredMixin,  UpdateView):
    template_name = 'posts/editar.html'
    model = Page
    form_class = ArticleForm
    context_object_name = 'article'
    success_url = '/blog'
     
    login_url = 'Login'

# -----------------------------------------------------------


class DeleteArticle (LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'posts/delete.html'
    context_object_name = 'blog'
    success_url = '/blog'
     
    login_url = 'Login'