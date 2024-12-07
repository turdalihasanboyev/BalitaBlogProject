from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Category


class CategoryPageView(View):
    template_name = 'category.html'

    def get(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        category = get_object_or_404(Category, slug__iexact=slug)
        articles = category.articles_category.all()
        context = {
            'category': category,
            'articles': articles,
        }
        return render(request, self.template_name, context)